import userProfile, tweetws
import datetime
from datetime import datetime, timezone
import time

def flip_detection(prof):
    today = datetime.now(timezone.utc)

    top = {}
    for t in prof.topics:
        top[t] = [[0,0],[0,0]]
    
    for tweet in prof.tweets:
        print((today - tweet.time).total_seconds())
        if (today - tweet.time).total_seconds() < 604800:
            print("New")
            if tweet.sentiment != "NONE":
                print("Succeed")
                for topics in tweet.topic:
                    top[topics][0][1] += 1
                    if tweet.sentiment == "P+":
                        top[topics][0][0] += 2
                    elif tweet.sentiment == "P":
                        top[topics][0][0] += 1
                    elif tweet.sentiment == "N":
                        top[topics][0][0] += -1
                    elif tweet.sentiment == "N+":
                        top[topics][0][0] += -2
        else:
            print("Old")
            if tweet.sentiment != "NONE":
                print("Succeed")
                for topics in tweet.topic:
                    top[topics][1][1] += 1
                    if tweet.sentiment == "P+":
                        top[topics][1][0] += 2
                    elif tweet.sentiment == "P":
                        top[topics][1][0] += 1
                    elif tweet.sentiment == "N":
                        top[topics][1][0] += -1
                    elif tweet.sentiment == "N+":
                        top[topics][1][0] += -2

    return top    
