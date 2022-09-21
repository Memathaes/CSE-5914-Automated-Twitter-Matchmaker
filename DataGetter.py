from abc import ABC, abstractmethod
from encodings import utf_8
import tweepy, csv

class DataGetter(ABC):
    @abstractmethod
    def get_Data(usrname):
        pass
    
    @abstractmethod
    def get_Matches(usrname):
        pass


class TwitterDataGetter(DataGetter):
    def get_Data(usrname, numberoftweets, client):
        if numberoftweets > 20:
            numberoftweets = 20
        elif numberoftweets < 10:
            numberoftweets = 10
        query = 'from:' + usrname + '   -is:retweet'
        results = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=numberoftweets)
        tweets = []
        if results.meta["result_count"] != 0:
            for tweet in results.data:
                tweets.append(tweet.text)
        return tweets
    
    def get_matches(usrname,numberoftweets,client):
        handles = []
        with open('Top-1000-Celebrity-Twitter-Accounts.csv',encoding="utf_8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                handles.append(row[0])
        dates = [21-1,767-1,47-1,294-1,16-1]
        for i in range(len(dates)):
            dates[i] = handles[dates[i]]

        results = {}
        for date in dates:
            results[date] = TwitterDataGetter.get_Data(date,numberoftweets,client)
        return results