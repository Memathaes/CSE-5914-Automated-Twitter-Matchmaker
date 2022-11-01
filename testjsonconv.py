import profile
import tweetws
import os
import json

fileName = "testDataBoogaloo.json"
Profiles = {}
if os.path.getsize(fileName) != 0:
    with open(fileName) as infile:
        Profiles = json.load(infile)

for prof in Profiles:
    Profiles[prof] = profile.from_json(Profiles[prof])

print(type(Profiles['halsey'].tweets[0].topic[0]))
print(Profiles['halsey'].tweets[0].topic)
