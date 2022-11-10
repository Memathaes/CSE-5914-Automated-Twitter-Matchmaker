import profile
import tweetws
import os
import json
import jsons
from elasticsearch import Elasticsearch
import config
import re

with open("blns.json", "r", encoding="utf8") as infile:
    strings = json.load(infile)


for naughtystring in strings:
    pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
    regex = pattern.match(naughtystring)
    if regex == None:
        print("The cake is a lie")
    else:
        print(regex)
    