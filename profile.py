import tweetws

class Profile:
    def __init__(self, username, tweets, sntmntTweets, avglen, positivity, topics):
        self.username = username
        self.tweets = tweets
        self.sntmntTweets = sntmntTweets
        self.avglen = avglen
        self.positivity = positivity
        self.topics = topics
    
def from_json(d):
    tempProf = Profile(d['username'], d['tweets'], d['sntmntTweets'], d['avglen'], d['positivity'], d['topics'])
    i = 0
    for tweet in tempProf.tweets:
        tempProf.tweets[i] = tweetws.from_json(tweet)
        i += 1
    return tempProf
