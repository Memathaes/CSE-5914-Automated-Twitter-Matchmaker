def simple(yourPositivity, yourTopics, Profiles, usr):

    sharedTopics = {}
    posDict = {}

    for potentialMatch in Profiles:
        if potentialMatch.lower() != usr.lower():
            theirProfile = Profiles[potentialMatch]
            theirPositivity = theirProfile['positivity']
            theirTopics = theirProfile['topics']

            sharedTopics[potentialMatch] = []
            posDict[potentialMatch] = theirPositivity
            for topic in theirTopics:
                if topic in yourTopics.keys():
                    sharedTopics[potentialMatch].append(topic)

    return [dict(sorted(sharedTopics.items(), key=lambda item: (abs(len(item[1])),3 - abs(yourPositivity - posDict[item[0]])),reverse=True)), posDict]