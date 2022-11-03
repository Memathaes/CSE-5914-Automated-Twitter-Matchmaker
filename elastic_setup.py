from elasticsearch import Elasticsearch
import config

import profile
import os
import json

ELASTIC_PASSWORD = config.elastic_pass

es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)




fileName = "testDataBoogaloo.json"
Profiles = {}
if os.path.getsize(fileName) != 0:
    with open(fileName) as infile:
        Profiles = json.load(infile)

# for prof in Profiles:
#     Profiles[prof] = profile.from_json(Profiles[prof])

#resp = es.index(index="test-index", id="hasley-test", document=json.dumps(Profiles["halsey"]))
#print(resp['result'])
something = es.get(index="test-index", id="hasley-test")
print(something['_source'])