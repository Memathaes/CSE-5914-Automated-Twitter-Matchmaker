import profile
import tweetws
import os
import json
import jsons
from elasticsearch import Elasticsearch
import config

ELASTIC_PASSWORD = config.elastic_pass
es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

usr = "halsey"
resp = es.search(index="profiles", query={"match_all": {}}, size=10000)
print("Got " + str(resp['hits']['total']['value']) + " hits")

for usr in resp['hits']['hits']:
    print(usr['_source']['username'])