import tweepy
import config
import DataGetter
import meaningcloud
import profile
import json
import jsons
import os


def ui(usr):

    client = tweepy.Client(bearer_token=config.bearer_token)
    tweetList = []

    fileName = "testDataBoogaloo.json"
    if os.path.getsize(fileName) != 0:
        file = open(fileName)
        Profiles = json.load(file)
        file.close()
    else:
        Profiles = {}

    numberofmatches = 10

    if usr.lower() in Profiles.keys():
        yourProfile = Profiles[usr.lower()]
        yourPositivity = yourProfile['positivity']
        yourTopics = yourProfile['topics']

        sharedTopics = {}
        posDict = {}
        for potentialMatch in Profiles:
            if potentialMatch != usr:
                theirProfile = Profiles[potentialMatch]
                theirPositivity = theirProfile['positivity']
                theirTopics = theirProfile['topics']

                sharedTopics[potentialMatch] = []
                posDict[potentialMatch] = theirPositivity
                for topic in theirTopics:
                    if topic in yourTopics.keys():
                        sharedTopics[potentialMatch].append(topic)
        matchesmade = dict(sorted(sharedTopics.items(), key=lambda item: (
            abs(len(item[1])), 3 - abs(yourPositivity - posDict[item[0]])), reverse=True))
        count = 0
        tweetList.append("Your Topics: " +
                         str(list(yourTopics.keys())))
        tweetList.append("Your Positivity: " +
                         str(round(yourPositivity, 3)))
        tweetList.append("")
        for match in matchesmade:
            if count == numberofmatches:
                break
            tweetList.append("Twitter handle: " + str(match))
            tweetList.append("Your Shared Topics: " + str(matchesmade[match]))
            tweetList.append("Shared Topic Count: " +
                             str(len(matchesmade[match])))
            tweetList.append("Their Positivity: " +
                             str(round(posDict[match], 3)))
            tweetList.append("Proximity to your Positivity: " +
                             str(round(posDict[match] - yourPositivity, 3)))
            tweetList.append("")
            count += 1

    else:
        tweetList.append(
            "Your twitter handle isn't in our database yet! Press \"Create/Update Profile\" to add yourself to it!")
    return tweetList


def u_click(usr):
    client = tweepy.Client(bearer_token=config.bearer_token)
    tweetList = []

    fileName = "testDataBoogaloo.json"
    if os.path.getsize(fileName) != 0:
        file = open(fileName)
        Profiles = json.load(file)
        file.close()
    else:
        Profiles = {}

    if usr.lower() in Profiles.keys():
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(
            usr, 25, client)
    else:
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(
            usr, 50, client)

    if len(yourTweets) > 0:
        if usr.lower() in Profiles.keys():
            tweetList.append("Updating your profile! This may take awhile...")

            Profiles[usr.lower()] = DataGetter.TwitterDataGetter.updateProfile(
                Profiles[usr.lower()], yourTweets)
            tweetList.append(
                "Your profile has been updated! You may now press \"Find Matches\"!")
        else:
            tweetList.append("Creating your profile! This may take awhile...")
            Profiles[usr.lower()] = DataGetter.TwitterDataGetter.generateProfile(
                usr.lower(), yourTweets)
            tweetList.append(
                "Your profile has been created! You may now press \"Find Matches\"!")
        with open(fileName, "w") as outfile:
            json.dump(jsons.dump(Profiles), outfile, indent=2)
    else:
        tweetList.append(
            "No tweets were found! Are you sure you entered the right username?")
    return
