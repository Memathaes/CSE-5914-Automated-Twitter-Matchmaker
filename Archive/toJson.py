import tweepy
import config
from elasticsearch import Elasticsearch
import jsons
import userProfile
import tweetws
import time
import json

ELASTIC_PASSWORD = config.elastic_pass
es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

resp = es.search(index="profiles4", query={"match_all": {}}, size=10000)
print("Got %d Hits:" % resp['hits']['total']['value'])
Profiles = {}
for prof in resp['hits']['hits']:
    user = prof['_source']
    yourProfile = jsons.load(user, userProfile.UserProfile)
    Profiles[yourProfile.username] = yourProfile
with open("newImportData2.json", "w") as outfile:
    json.dump(jsons.dump(Profiles), outfile, indent=2)
