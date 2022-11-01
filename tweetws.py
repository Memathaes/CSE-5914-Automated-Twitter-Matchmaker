from os import stat

class Tweetws:
    def __init__(self, tID, tweetText, length, sentiment, topic):
        self.tID = tID
        self.tweetText = tweetText
        self.length = length
        self.sentiment = sentiment
        self.topic = topic
    
def from_json(t):
    return Tweetws(t['tID'], t['tText'], t['length'], t['sentiment'], t['topic'])
