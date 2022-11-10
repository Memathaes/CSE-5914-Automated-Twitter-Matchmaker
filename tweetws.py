class Tweetws:
    def __init__(self, tID, tText, length, sentiment, topic):
        self.tID = tID
        self.tText = tText
        self.length = length
        self.sentiment = sentiment
        self.topic = topic
    
def from_json(t):
    return Tweetws(t['tID'], t['tText'], t['length'], t['sentiment'], t['topic'])
