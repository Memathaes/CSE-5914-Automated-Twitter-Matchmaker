import profile
import tweetws
import os
import json
import jsons
from elasticsearch import Elasticsearch
import config
import re

ELASTIC_PASSWORD = config.elastic_pass
es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

# topic = "Halsey"
# field_str = "topics." + topic
# resp = es.search(index="profiles", query={"exists": {"field": field_str}}, size=10000)
# print("Got %d Hits:" % resp['hits']['total']['value'])

# for hit in resp['hits']['hits']:
#     print(hit["_source"]['username'])

user = es.get(index="profiles", id="potus")
yourProfile = jsons.load(user['_source'], profile.Profile)
yourTopics = yourProfile.topics

Profiles = {}
for topic in yourTopics:
    field_str = "topics." + topic
    resp = es.search(index="profiles", query={"exists": {"field": field_str}}, size=10000)
    for person in resp['hits']['hits']:
        otherUser = person['_source']['username']
        if otherUser != yourProfile.username:
            if otherUser in Profiles.keys():
                Profiles[otherUser][1] += 1
            else:
                Profiles[otherUser] = [person['_source'],1]

            if yourTopics[topic][1] != 0 and person['_source']['topics'][topic][1] != 0:
                reduction = (abs((yourTopics[topic][2] / yourTopics[topic][1]) - (person['_source']['topics'][topic][2] / person['_source']['topics'][topic][1])) / 2) ** 1.5
                Profiles[otherUser][1] -= reduction
            else:
                Profiles[otherUser][1] -= 1
newdict = dict(sorted(Profiles.items(), key=lambda item: item[1][1], reverse=True))

for prof in newdict:
    print(newdict[prof][1])

# with open("blns.json", "r", encoding="utf8") as infile:
#     strings = json.load(infile)

# for naughtystring in strings:
#     pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
#     regex = pattern.match(naughtystring)
#     if regex != None:
#         print(es.exists(index="profiles", id=naughtystring))