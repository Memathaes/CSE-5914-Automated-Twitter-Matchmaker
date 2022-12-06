import datetime

class Tweetws:
    def __init__(self, tID, tText, length, sentiment, topic, time:datetime.datetime):
        self.tID = tID
        self.tText = tText
        self.length = length
        self.sentiment = sentiment
        self.topic = topic
        self.time = time
