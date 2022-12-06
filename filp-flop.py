import profile, tweetws
import datetime
from datetime import date

def flip_detection(prof = profile()):
    today = date.today()
    flip = {prof.username : []}

    top = {}
    for t in prof.topics:
        
        top[t] = [0,0]
    
    for tweet in prof.tweets:
        if (today - tweet.time).total_seconds()/60 < 604800:
            if tweet.sentiment != "NONE":
                #top[tweet.topic][0] = 0
                if tweet.sentimen == "P+":
                    top[tweet.topic][0] += 2
                elif tweet.sentimen == "P":
                    top[tweet.topic][0] += 1
                elif tweet.sentimen == "N":
                    top[tweet.topic][0] += -1
                elif tweet.sentimen == "N+":
                    top[tweet.topic][0] += -2
            else:
                if tweet.sentimen == "P+":
                    top[tweet.topic][1] += 2
                elif tweet.sentimen == "P":
                    top[tweet.topic][1] += 1
                elif tweet.sentimen == "N":
                    top[tweet.topic][1] += -1
                elif tweet.sentimen == "N+":
                    top[tweet.topic][1] += -2
        
    flip[prof.username].append(top)

    return flip    
