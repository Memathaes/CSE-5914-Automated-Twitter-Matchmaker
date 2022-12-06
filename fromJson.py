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

Profiles = {}
with open("newImportData.json", "r") as infile:
    Profiles = json.load(infile)

for prof in Profiles:
    es.index(index="from-json", id=prof, document=Profiles[prof])
