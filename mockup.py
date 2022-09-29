import time, tweepy, config
import tkinter as tk
from simplemagic import sm
import DataGetter
import meaningcloud

class Profile:
    def __init__(self, username, tweets, avglen, topics, positivity):
        self.username = username
        self.tweets = tweets
        self.avglen = avglen
        self.topics = topics
        self.positivity = positivity

def main():

    client = tweepy.Client(bearer_token=config.bearer_token)

    Profiles = []
    matches = DataGetter.TwitterDataGetter.get_data(10,client)
    for potential in matches:
        avglen = 0
        numtweet = 0
        for tweet in matches[potential]:
            avglen = avglen + len(tweet)
            numtweet = numtweet + 1
        if numtweet != 0:
            avglen = avglen / numtweet
        Profiles.append(Profile(potential, matches[potential],avglen,0,0))

    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    greeting = tk.Label(text="MVP UI")

    #greeting.pack()
    greeting.grid(row=0,column=1)

    label1 = tk.Label(text="Enter Your Username:")
    e = tk.Entry()


    label2 = tk.Label(text="Enter how many matches you want:")
    output = tk.Entry()

    tweetList = tk.Listbox(width=150, height=30)

    def e_click():
        tweetList.delete(0,tk.END)
        usr = e.get()
        numberofmatches = int(output.get())
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,10,client)

        avglen = 0
        numtweet = 0
        for tweet in yourTweets:
            avglen = avglen + len(tweet)
            numtweet = numtweet + 1
        avglen = avglen / numtweet
        yourProfile = Profile(usr,yourTweets,avglen,0,0)



        lengthsim = {}
        for pot in Profiles:
            lengthsim.update({pot.username: pot.avglen - yourProfile.avglen})
        matchesmade = dict(sorted(lengthsim.items(), key=lambda item: abs(item[1])))
        count = 0
        tweetList.insert(tk.END,"Your Average Tweet Length: " + str(round(yourProfile.avglen,1)))
        tweetList.insert(tk.END,"")
        for match in matchesmade:
            tweetList.insert(tk.END,"Twitter handle: " + str(match))
            tweetList.insert(tk.END,"Average Tweet Length: " + str(round(matchesmade[match] + yourProfile.avglen,1)))
            tweetList.insert(tk.END,"Closeness to your length: " + str(round(matchesmade[match],1)))
            tweetList.insert(tk.END,"")
            count +=1
            if count == numberofmatches:
                break
        return 

    enter = tk.Button(
        text="Enter",
        command = e_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    label1.grid(row = 2, column = 0,padx=5,pady=5)
    e.grid(row=2,column=1,padx=5,pady=5)

    label2.grid(row = 3, column = 0,padx=5,pady=5)
    output.grid(row=3,column=1,padx=5,pady=5)

    enter.grid(row=2, column=3,padx=5,pady=5)
    tweetList.grid(row = 4, column = 1,padx=5,pady=5)

    window.mainloop()

if __name__ == "__main__": main()