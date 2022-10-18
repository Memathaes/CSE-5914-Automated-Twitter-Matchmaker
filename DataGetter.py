from abc import ABC, abstractmethod
from encodings import utf_8
import tweepy, csv, json, jsons, datetime, time, config, os
import profile, tweetws
import meaningcloud as mc

class DataGetter(ABC):
    @abstractmethod
    def get_data(usrname):
        pass
    
    @abstractmethod
    def get_users_tweets(usrname):
        pass


class TwitterDataGetter(DataGetter):
    def get_users_tweets(usrname, numberoftweets, client, previousRetrieval = "2010-11-06T00:00:00Z"):
        if numberoftweets > 20:
            numberoftweets = 20
        elif numberoftweets < 10:
            numberoftweets = 10
        Id = client.get_user(username = usrname).data.id
        results = client.get_users_tweets(id=Id,max_results = numberoftweets, exclude = "retweets,replies",start_time = previousRetrieval) 
        
        tweets = []
        if results.meta["result_count"] != 0:
            for tweet in results.data:
                tweets.insert(0,[tweet.id, tweet.text])
        return tweets
    
    def updateProfile(prevProfile, newTweets):
        avglen = prevProfile['avglen'] * len(prevProfile['tweets'])
        numtweet = len(prevProfile['tweets'])
        sentimentScore = prevProfile['positivity']
        sentimentedTweets = prevProfile['sntmntTweets']
        topics = prevProfile['topics']
        tweetsWithData = prevProfile['tweets']

        for tweet in newTweets:
            if tweet[0] > tweetsWithData[0]['tID']:
                avglen = avglen + len(tweet[1])
                numtweet = numtweet + 1

                top = mc.ClassResponse(mc.ClassRequest(config.mc_token, txt = tweet[1], model='SocialMedia_en').sendReq())
                time.sleep(1)
                topic = top.getCategories()

                sent = mc.SentimentResponse(mc.SentimentRequest(config.mc_token, txt = tweet[1], lang='en').sendReq())
                time.sleep(1)
                score = sent.getGlobalScoreTag()

                tweetsWithData.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),topic,score))

                sentimentIncrement = 0
                if (score != "NONE"):
                    sentimentedTweets += 1
                    if (score == "P+"):
                        sentimentIncrement = 2
                    elif (score == "P"):
                        sentimentIncrement = 1
                    elif (score == "N"):
                        sentimentIncrement = -1
                    elif (score == "N+"):
                        sentimentIncrement = -2
                    sentimentScore += sentimentIncrement
                
                for elem in topic:
                    if elem['label'] in topics:
                        topics[elem['label']][0] += 1
                        topics[elem['label']][1] += sentimentIncrement
                    else:
                        topics[elem['label']] = [1, sentimentIncrement]
        if numtweet != 0:
            avglen = avglen / numtweet
        return profile.Profile(prevProfile['username'],tweetsWithData,avglen,topics,sentimentScore,sentimentedTweets)
    
    def generateProfile(username, tweets):
        avglen = 0
        numtweet = 0
        sentimentScore = 0.0
        sentimentedTweets = 0
        topics = {}
        tweetsWithData = []
        for tweet in tweets:
            avglen = avglen + len(tweet[1])
            numtweet = numtweet + 1

            top = mc.ClassResponse(mc.ClassRequest(config.mc_token, txt = tweet[1], model='SocialMedia_en').sendReq())
            time.sleep(1)
            topic = top.getCategories()

            sent = mc.SentimentResponse(mc.SentimentRequest(config.mc_token, txt = tweet[1], lang='en').sendReq())
            time.sleep(1)
            score = sent.getGlobalScoreTag()

            tweetsWithData.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),topic,score))

            sentimentIncrement = 0
            if (score != "NONE"):
                sentimentedTweets += 1
                if (score == "P+"):
                    sentimentIncrement = 2
                elif (score == "P"):
                    sentimentIncrement = 1
                elif (score == "N"):
                    sentimentIncrement = -1
                elif (score == "N+"):
                    sentimentIncrement = -2
                sentimentScore += sentimentIncrement

            for elem in topic:
                if elem['label'] in topics:
                    topics[elem['label']][0] += 1
                    topics[elem['label']][1] += sentimentIncrement
                else:
                    topics[elem['label']] = [1, sentimentIncrement]
        if numtweet != 0:
            avglen = avglen / numtweet

        return profile.Profile(username,tweetsWithData,avglen,topics,sentimentScore,sentimentedTweets)
    
    def get_data(numberoftweets,client):
        handles = []
        with open('Top-1000-Celebrity-Twitter-Accounts.csv',encoding="utf_8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                handles.append(row[0])
        #dates = [21-1,767-1,47-1,294-1,16-1,5-1,27-1,34-1,35-1,44-1,51-1,83-1,102-1]
        dates = ["KimKardashian","ElonMusk","NICKIMINAJ","POTUS","Halsey"]
        #for i in range(len(dates)):
            #dates[i] = handles[dates[i]]

        fileName = "testDataBoogaloo.json"
        if os.path.getsize(fileName) != 0:
            file = open(fileName)
            data = json.load(file)
            file.close()
        else:
            data = {}

        for date in dates:
            print("Getting " + date)
            #if date in data:
                #results = TwitterDataGetter.get_users_tweets(date,numberoftweets,client,data[date].pop())
            #else:
            results = TwitterDataGetter.get_users_tweets(date,numberoftweets,client)

            if date.lower() in data.keys():
                print("updating")
                data[date.lower()] = TwitterDataGetter.updateProfile(data[date.lower()], results)
            else:
                print("creating")
                data[date.lower()] = TwitterDataGetter.generateProfile(date.lower(), results)

            #data[date] = list(dict.fromkeys(data[date])) 
            #data[date].append(str(datetime.datetime.now().isoformat())[:-7]+"Z")

        print("writing to file")
        with open(fileName, "w") as outfile:
            json.dump(jsons.dump(data),outfile,indent=2)