import tweetws

class UserProfile:
    def __init__(self, username, tweets:list[tweetws.Tweetws], sntmntTweets, avglen, positivity, topics):
        self.username = username
        self.tweets = tweets
        self.sntmntTweets = sntmntTweets
        self.avglen = avglen
        self.positivity = positivity
        self.topics = topics
    