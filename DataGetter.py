from abc import ABC, abstractmethod

class DataGetter(ABC):
    @abstractmethod
    def get_Data(usrname):
        pass


class TwitterDataGetter(DataGetter):
    def get_Data(usrname, client):
        query = 'from:' + usrname + ' -is:retweet'
        tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=10)
        return tweets