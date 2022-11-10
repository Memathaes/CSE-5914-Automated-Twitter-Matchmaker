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
ELASTIC_PASSWORD = config.elastic_pass

def ui(usr):
    tweetList = []

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
    tweetList = []
    es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)
    client = tweepy.Client(bearer_token=config.bearer_token)

    pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
    regex = pattern.match(usr)

    if regex is None:
        print("aaaaaaaaaaa")
        tweetList.append("Your username doesn't match twitter username format!")
        return tweetList

    usr = usr.lower()
    if es.exists(index="profiles", id=usr):
        user = es.get(index="profiles", id=usr)
        Profile = jsons.load(user['_source'], profile.Profile)
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,25,client)
        if len(yourTweets) > 0:
            tweetList.append("Updating your profile! This may take awhile...")
            Profile = DataGetter.TwitterDataGetter.updateProfile(Profile, yourTweets)
            tweetList.append("Your profile has been updated! You may now press \"Find Matches\"!")
        else:
            tweetList.append("No tweets were found! Are you sure you entered the right username?")
    else:
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,50,client)
        if len(yourTweets) > 0:
            tweetList.append("Creating your profile! This may take awhile...")
            Profile = DataGetter.TwitterDataGetter.generateProfile(usr, yourTweets)
            tweetList.append("Your profile has been created! You may now press \"Find Matches\"!")
        else:
            tweetList.append("No tweets were found! Are you sure you entered the right username?")
    
    es.index(index="profiles", id=usr, document=jsons.dumps(Profile))
    return tweetList
