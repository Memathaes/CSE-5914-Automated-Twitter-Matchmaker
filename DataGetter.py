from abc import ABC, abstractmethod
from encodings import utf_8
import tweepy, csv, json, jsons, datetime, time, config, os
import userProfile, tweetws
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
        results = client.get_users_tweets(id=Id,max_results = numberoftweets, exclude = "retweets,replies",start_time = previousRetrieval,tweet_fields = ["context_annotations","created_at"])
        
        tweets = []
        if results.meta["result_count"] != 0:
            for tweet in results.data:
                tweets.insert(0,[tweet.id, tweet.text, tweet.context_annotations,tweet.created_at])
        return tweets
    
    @staticmethod
    def updateProfile(Profile, newTweets):
        Profile.avglen = Profile.avglen * len(Profile.tweets)
        Profile.positivity = Profile.positivity * len(Profile.sntmntTweets)

        latestID = Profile.tweets[0].tID

        for tweet in newTweets:
            if tweet[0] > latestID:
                Profile.avglen = Profile.avglen + len(tweet[1])

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
                    Profile.positivity += sentimentIncrement
                    Profile.sntmntTweets.insert(0,[tweet[0],sentimentIncrement])
                
                theseTopics = []
                for topic in tweet[2]:
                    if topic['domain']['id'] == '131':
                        theseTopics.append(topic['entity']['name'])
                        if not topic['entity']['name'] in Profile.topics.keys():
                            Profile.topics[topic['entity']['name']] = [0,0,0]
                
                Profile.tweets.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),score,theseTopics,tweet[3]))
                
                for elem in theseTopics:
                    Profile.topics[elem][0] += 1
                    if score != "NONE":
                        Profile.topics[elem][1] += 1
                        Profile.topics[elem][2] += sentimentIncrement
        if len(Profile.tweets) != 0:
            Profile.avglen = Profile.avglen / len(Profile.tweets)
        if len(Profile.sntmntTweets) != 0:
            Profile.positivity = Profile.positivity / len(Profile.sntmntTweets)

        return Profile
    
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
            
            tweetsWithData.insert(0,tweetws.Tweetws(tweet[0],tweet[1],len(tweet[1]),score,theseTopics,tweet[3]))

            for elem in theseTopics:
                topics[elem][0] += 1
                if score != "NONE":
                    topics[elem][1] += 1
                    topics[elem][2] += sentimentIncrement
        if len(tweetsWithData) != 0:
            avglen = avglen / len(tweetsWithData)
        if len(sentimentedTweets) != 0:
            sentimentScore = sentimentScore / len(sentimentedTweets)

        return userProfile.UserProfile(username,tweetsWithData,sentimentedTweets,avglen,sentimentScore,topics)
    
    @staticmethod
    def get_data(client,es):
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
        dates = ["Elonmusk"]

        for date in dates:
            usr = date.lower()
            print("Getting " + usr)
            if es.exists(index="profiles4", id=usr):
                user = es.get(index="profiles4", id=usr)
                Profile = jsons.load(user['_source'], userProfile.UserProfile)
                yourTweets = TwitterDataGetter.get_users_tweets(usr,25,client)
                if len(yourTweets) > 0:
                    print("Creating " + usr)
                    Profile = TwitterDataGetter.updateProfile(Profile, yourTweets)
            else:
                yourTweets = TwitterDataGetter.get_users_tweets(usr,50,client)
                if len(yourTweets) > 0:
                    print("Creating " + usr)
                    Profile = TwitterDataGetter.generateProfile(usr, yourTweets)
            resp = es.index(index="profiles4", id=usr, document=jsons.dumps(Profile))
            print(resp)
