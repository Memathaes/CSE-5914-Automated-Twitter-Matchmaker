import tweepy
import config
import DataGetter
import meaningcloud
import userProfile
import json
import jsons
import os
from elasticsearch import Elasticsearch
import matching
import re
import flipflop
ELASTIC_PASSWORD = config.elastic_pass

#find matches button
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
    if es.exists(index="profiles4", id=usr):
        user = es.get(index="profiles4", id=usr)
        yourProfile = jsons.load(user['_source'], userProfile.UserProfile)
        
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
        tweetList.append("Your twitter handle isn't in our database yet!")
    return tweetList

#update database button
def u_click(usr):
    tweetList = []
    es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)
    client = tweepy.Client(bearer_token=config.bearer_token)

    pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
    regex = pattern.match(usr)

    if regex is None:
        tweetList.append("Your username doesn't match twitter username format!")
        return tweetList

    usr = usr.lower()
    if es.exists(index="profiles4", id=usr):
        print("hello")
        user = es.get(index="profiles4", id=usr)
        Profile = jsons.load(user['_source'], userProfile.UserProfile)
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,25,client)
        if len(yourTweets) > 0:
            Profile = DataGetter.TwitterDataGetter.updateProfile(Profile, yourTweets)
            tweetList.append("Your profile has been updated!")
            es.index(index="profiles5", id=usr, document=jsons.dumps(Profile))
        else:
            tweetList.append("No tweets were found! Are you sure you entered the right username?")
    else:
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,50,client)
        if len(yourTweets) > 0:
            Profile = DataGetter.TwitterDataGetter.generateProfile(usr, yourTweets)
            tweetList.append("Your profile has been created!")
            es.index(index="profiles5", id=usr, document=jsons.dumps(Profile))
        else:
            tweetList.append("No tweets were found! Are you sure you entered the right username?")
    return tweetList

#find matches button
def flipper(usr):
    tweetList = []

    es = Elasticsearch(hosts = 'https://localhost:9200' , basic_auth=["elastic", ELASTIC_PASSWORD], verify_certs=False)

    pattern = re.compile("^[a-zA-Z0-9_]{1,15}$")
    regex = pattern.match(usr)
    if regex is None:
        tweetList.append("Your username doesn't match twitter username format!")
        return tweetList

    usr = usr.lower()
    if es.exists(index="profiles5", id=usr):
        user = es.get(index="profiles5", id=usr)
        yourProfile = jsons.load(user['_source'], userProfile.UserProfile)
        
        timesliceTopics = flipflop.flip_detection(yourProfile)
        tweetList.append("Your Handle: " + yourProfile.username)
        tweetList.append("")
        for topic in timesliceTopics:
            if timesliceTopics[topic][0][1] != 0 and timesliceTopics[topic][1][1] != 0:
                tweetList.append("Topic: " + str(topic) + ". This week score: " + str(timesliceTopics[topic][0][0] / timesliceTopics[topic][0][1]) + ". Last week score: " + str(timesliceTopics[topic][1][0] / timesliceTopics[topic][1][1]))
                tweetList.append("")
    else:
        tweetList.append("Your twitter handle isn't in our database yet!")
    return tweetList
