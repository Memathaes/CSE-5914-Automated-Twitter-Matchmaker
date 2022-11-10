import tweepy
import config
import DataGetter
import meaningcloud
import profile
import json
import jsons
import os
from elasticsearch import Elasticsearch
import matching
import re


def ui(usr):

    ELASTIC_PASSWORD = config.elastic_pass
    tweetList = []

    client = tweepy.Client(bearer_token=config.bearer_token)
    es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

    pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
    regex = pattern.match(usr)
    if regex is None:
        tweetList.append("Your username doesn't match twitter username format!")
        return tweetList

    numberofmatches = 10
    usr = usr.lower()
    if es.exists(index="profiles", id=usr):
        user = es.get(index="profiles", id=usr)
        yourProfile = jsons.load(user['_source'], profile.Profile)
        
        matchesmade = matching.magic(yourProfile, es)
        count = 0
        tweetList.append("Your Handle: " + yourProfile.username)
        tweetList.append("")
        for match in matchesmade:
            if count == numberofmatches:
                break
            tweetList.append("Twitter handle: " + str(match))
            tweetList.append("Your Compatibility Score: " + str(matchesmade[match][1]))
            tweetList.append("")
            count +=1
    else:
        tweetList.append("Your twitter handle isn't in our database yet! Press \"Create/Update Profile\" to add yourself to it!")
    return tweetList


def u_click(usr):
    client = tweepy.Client(bearer_token=config.bearer_token)
    tweetList = []

    fileName = "testDataBoogaloo.json"
    if os.path.getsize(fileName) != 0:
        with open(fileName) as infile:
            Profiles = json.load(infile)
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
    return tweetList
