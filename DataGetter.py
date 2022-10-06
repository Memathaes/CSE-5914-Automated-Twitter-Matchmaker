from abc import ABC, abstractmethod
from encodings import utf_8
import tweepy, csv, json, datetime

class DataGetter(ABC):
    @abstractmethod
    def get_data(usrname):
        pass
    
    @abstractmethod
    def get_users_tweets(usrname):
        pass


class TwitterDataGetter(DataGetter):
    def get_users_tweets(usrname, numberoftweets, client, previousRetrieval):
        if numberoftweets > 20:
            numberoftweets = 20
        elif numberoftweets < 10:
            numberoftweets = 10
        Id = client.get_user(username = usrname).data.id
        results = client.get_users_tweets(id=Id,max_results = 100, exclude = "retweets,replies",start_time = previousRetrieval) 
        
        tweets = []
        print(results)
        if results.meta["result_count"] != 0:
            for tweet in results.data:
                tweets.append(tweet.text)
        return tweets
    
    def get_data(numberofmatches,client):
        handles = []
        with open('Top-1000-Celebrity-Twitter-Accounts.csv',encoding="utf_8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                handles.append(row[0])
        dates = [21-1,767-1,47-1,294-1,16-1,5-1,27-1,34-1,35-1,44-1,51-1,83-1,102-1]
        for i in range(len(dates)):
            dates[i] = handles[dates[i]]

        fileName = "userData.json"
        file = open(fileName)
        data = json.load(file)
        file.close()
        for date in dates:
            results = TwitterDataGetter.get_users_tweets(date,10,client,data[date].pop())
            for tweet in results:
                data[date].append(tweet)
                
            data[date] = list(dict.fromkeys(data[date])) 
            data[date].append(str(datetime.datetime.now().isoformat())[:-7]+"Z")

        with open(fileName, "w") as outfile:
            json.dump(data,outfile,indent=2)

        return data