def magic(yourProfile, es):
    yourTopics = yourProfile.topics

    Profiles = {}
    for topic in yourTopics:
        field_str = "topics." + topic
        resp = es.search(index="profiles4", query={"exists": {"field": field_str}}, size=10000)
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
    scoredDict = dict(sorted(Profiles.items(), key=lambda item: item[1][1], reverse= True))
    maxScore = 0
    for person in scoredDict:
        if maxScore == 0:
            maxScore = scoredDict[person][1]
        scoredDict[person][1] /= maxScore
    return scoredDict
