import profile
import tweetws
import os
import json

fileName = "testDataBoogaloo.json"
if os.path.getsize(fileName) != 0:
    with open(fileName) as infile:
        Profiles = json.load(infile)
