import tweepy
import config
from elasticsearch import Elasticsearch
import jsons
import userProfile
import tweetws
import time

#No need to run again

ELASTIC_PASSWORD = config.elastic_pass
es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

client = tweepy.Client(bearer_token=config.bearer_token,wait_on_rate_limit=True)

# es.delete(index="profiles",id="guppisound")
# es.delete(index="profiles2",id="guppisound")

AlreadyIn = []
resp = es.search(index="profiles4", query={"match_all": {}}, size=10000)
print("Got %d Hits:" % resp['hits']['total']['value'])
for prof in resp['hits']['hits']:
    user = prof['_source']
    yourProfile = jsons.load(user, userProfile.UserProfile)
    AlreadyIn.append(yourProfile.username)
    print(yourProfile.username)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

resp = es.search(index="profiles", query={"match_all": {}}, size=10000)
print("Got %d Hits:" % resp['hits']['total']['value'])
for prof in resp['hits']['hits']:
    user = prof['_source']
    yourProfile = jsons.load(user, userProfile.UserProfile)
    if yourProfile.username not in AlreadyIn:
        i = 0
        for tweet in yourProfile.tweets:
            yourProfile.tweets[i] = jsons.load(tweet, tweetws.Tweetws)
            i += 1
        i = 0
        for tweet in yourProfile.tweets:
            newTweet = client.get_tweet(tweet.tID, tweet_fields = "created_at")
            if newTweet.data != None:
                yourProfile.tweets[i].time = newTweet.data.created_at
            i += 1
        AlreadyIn.append(yourProfile.username)
        print("sending " + yourProfile.username)
        es.index(index="profiles4", id=yourProfile.username, document=jsons.dumps(yourProfile))
        print("sent")
    else:
        print(yourProfile.username + " Already in!")


