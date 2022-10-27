from abc import ABC, abstractmethod
from encodings import utf_8
import tweepy, csv, json, jsons, datetime, time, config, os
import profile, tweetws
import meaningcloud as mc

class TwitterDataGetter:
    @staticmethod
    def get_users_tweets(usrname, numberoftweets, client, previousRetrieval = "2010-11-06T00:00:00Z"):
        if numberoftweets > 100:
            numberoftweets = 100
        elif numberoftweets < 10:
            numberoftweets = 10
        apireq = client.get_user(username = usrname)
        tweets = []

        if apireq.data is None:
            return tweets

        Id = apireq.data.id
        results = client.get_users_tweets(id=Id,max_results = numberoftweets, exclude = "retweets,replies",start_time = previousRetrieval,tweet_fields = "context_annotations")
        
        tweets = []
        if results.meta["result_count"] != 0:
            for tweet in results.data:
                tweets.insert(0,[tweet.id, tweet.text, tweet.context_annotations])
        return tweets
    
    @staticmethod
    def updateProfile(prevProfile, newTweets):
        tweetsWithData = prevProfile['tweets']
        sentimentedTweets = prevProfile['sntmntTweets']
        avglen = prevProfile['avglen'] * len(tweetsWithData)
        sentimentScore = prevProfile['positivity'] * len(sentimentedTweets)
        topics = prevProfile['topics']

        latestID = tweetsWithData[0]['tID']

        for tweet in newTweets:
            if tweet[0] > latestID:
                avglen = avglen + len(tweet[1])

                sent = mc.SentimentResponse(mc.SentimentRequest(config.mc_token, txt = tweet[1], lang='en').sendReq())
                time.sleep(0.5)
                score = sent.getGlobalScoreTag()

                if score != "NONE":
                    sentimentIncrement = 0
                    if score == "P+":
                        sentimentIncrement = 2
                    elif score == "P":
                        sentimentIncrement = 1
                    elif score == "N":
                        sentimentIncrement = -1
                    elif score == "N+":
                        sentimentIncrement = -2
                    sentimentScore += sentimentIncrement
                    sentimentedTweets.insert(0,[tweet[0],sentimentIncrement])
                
                theseTopics = []
                for topic in tweet[2]:
                    if topic['domain']['id'] == '131':
                        theseTopics.append(topic['entity']['name'])
                        if not topic['entity']['name'] in topics.keys():
                            topics[topic['entity']['name']] = [0,0,0]
                
                tweetsWithData.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),score,theseTopics))
                
                for elem in theseTopics:
                    topics[elem][0] += 1
                    if score != "NONE":
                        topics[elem][1] += 1
                        topics[elem][2] += sentimentIncrement
        if len(tweetsWithData) != 0:
            avglen = avglen / len(tweetsWithData)
        if len(sentimentedTweets) != 0:
            sentimentScore = sentimentScore / len(sentimentedTweets)

        return profile.Profile(prevProfile['username'],tweetsWithData,sentimentedTweets,avglen,sentimentScore,topics)
    
    @staticmethod
    def generateProfile(username, tweets):
        tweetsWithData = []
        sentimentedTweets = []
        avglen = 0
        sentimentScore = 0.0
        topics = {}

        for tweet in tweets:
            avglen = avglen + len(tweet[1])

            sent = mc.SentimentResponse(mc.SentimentRequest(config.mc_token, txt = tweet[1], lang='en').sendReq())
            time.sleep(0.5)
            score = sent.getGlobalScoreTag()

            if score != "NONE":
                sentimentIncrement = 0
                if score == "P+":
                    sentimentIncrement = 2
                elif score == "P":
                    sentimentIncrement = 1
                elif score == "N":
                    sentimentIncrement = -1
                elif score == "N+":
                    sentimentIncrement = -2
                sentimentScore += sentimentIncrement
                sentimentedTweets.insert(0,[tweet[0],sentimentIncrement])
            
            theseTopics = []
            for topic in tweet[2]:
                if topic['domain']['id'] == '131' and not topic['entity']['name'] in theseTopics:
                    theseTopics.append(topic['entity']['name'])
                    if not topic['entity']['name'] in topics.keys():
                        topics[topic['entity']['name']] = [0,0,0]
            
            tweetsWithData.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),score,theseTopics))

            for elem in theseTopics:
                topics[elem][0] += 1
                if score != "NONE":
                    topics[elem][1] += 1
                    topics[elem][2] += sentimentIncrement
        if len(tweetsWithData) != 0:
            avglen = avglen / len(tweetsWithData)
        if len(sentimentedTweets) != 0:
            sentimentScore = sentimentScore / len(sentimentedTweets)

        return profile.Profile(username,tweetsWithData,sentimentedTweets,avglen,sentimentScore,topics)
    
    @staticmethod
    def get_data(numberoftweets,client):
        #handles = []
        #with open('Top-1000-Celebrity-Twitter-Accounts.csv',encoding="utf_8") as csv_file:
            #csv_reader = csv.reader(csv_file, delimiter=',')
            #for row in csv_reader:
                #handles.append(row[0])
        #dates = [21-1,767-1,47-1,294-1,16-1,5-1,27-1,34-1,35-1,44-1,51-1,83-1,102-1]
        #dates = ["nyjets","ElonMusk","NICKIMINAJ","POTUS","Halsey"]
        #for i in range(len(dates)):
            #dates[i] = handles[dates[i]]

        #Put any accounts you want to generate profiles for
        dates = ["Elonmusk","KimKardashian","TheEllenShow","KylieJenner","JimmyFallon"]

        fileName = "testDataBoogaloo.json"
        if os.path.getsize(fileName) != 0:
            file = open(fileName)
            data = json.load(file)
            file.close()
        else:
            data = {}

        for date in dates:
            print("Getting " + date)
            if date.lower() in data.keys():
                results = TwitterDataGetter.get_users_tweets(date,25,client)
            else:
                results = TwitterDataGetter.get_users_tweets(date,numberoftweets,client)

            if len(results) > 0:
                if date.lower() in data.keys():
                    print("updating " + date)
                    data[date.lower()] = TwitterDataGetter.updateProfile(data[date.lower()], results)
                else:
                    print("creating " + date)
                    data[date.lower()] = TwitterDataGetter.generateProfile(date.lower(), results)

            #data[date] = list(dict.fromkeys(data[date])) 
            #data[date].append(str(datetime.datetime.now().isoformat())[:-7]+"Z")

        print("writing to file")
        with open(fileName, "w") as outfile:
            json.dump(jsons.dump(data),outfile,indent=2)
