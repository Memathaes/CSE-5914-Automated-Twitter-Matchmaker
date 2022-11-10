class Tweetws:
    def __init__(self, tID, tweetText, length, sent, topic):
        self.tID = tID
        self.tText = tweetText
        self.length = length
        self.sentiment = sent
        self.topic = topic

def from_json(t):
    return Tweetws(t['tID'], t['tText'], t['length'], t['sentiment'], t['topic'])
