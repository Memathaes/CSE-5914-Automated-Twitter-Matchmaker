import time, tweepy, config
import tkinter as tk
import DataGetter
import meaningcloud
import profile
import json, jsons, os


def main():

    client = tweepy.Client(bearer_token=config.bearer_token)

    getdata = input("yes to add/update profiles: ")
    if (getdata == "yes"):
        DataGetter.TwitterDataGetter.get_data(50,client)

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

        fileName = "testDataBoogaloo.json"
        if os.path.getsize(fileName) != 0:
            file = open(fileName)
            Profiles = json.load(file)
            file.close()
        else:
            Profiles = {}

        usr = e.get()
        numInput = output.get()

        if numInput.isnumeric():
            numberofmatches = int(numInput)
        else:
            tweetList.insert(tk.END,"Invalid number of matches inputted!")
            return
            
        if usr.lower() in Profiles.keys():
            yourProfile = Profiles[usr.lower()]
            yourPositivity = yourProfile['positivity']
            yourTopics = yourProfile['topics']

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
            matchesmade = dict(sorted(sharedTopics.items(), key=lambda item: (abs(len(item[1])),3 - abs(yourPositivity - posDict[item[0]])),reverse=True))
            count = 0
            tweetList.insert(tk.END,"Your Topics: " + str(list(yourTopics.keys())))
            tweetList.insert(tk.END,"Your Positivity: " + str(round(yourPositivity,3)))
            tweetList.insert(tk.END,"")
            for match in matchesmade:
                if count == numberofmatches:
                    break
                tweetList.insert(tk.END,"Twitter handle: " + str(match))
                tweetList.insert(tk.END,"Your Shared Topics: " + str(matchesmade[match]))
                tweetList.insert(tk.END,"Shared Topic Count: " + str(len(matchesmade[match])))
                tweetList.insert(tk.END,"Their Positivity: " + str(round(posDict[match],3)))
                tweetList.insert(tk.END,"Proximity to your Positivity: " + str(round(posDict[match] - yourPositivity,3)))
                tweetList.insert(tk.END,"")
                count +=1
        else:
            tweetList.insert(tk.END,"Your twitter handle isn't in our database yet! Press \"Create/Update Profile\" to add yourself to it!")
        return
    
    def u_click():
        tweetList.delete(0,tk.END)

        fileName = "testDataBoogaloo.json"
        if os.path.getsize(fileName) != 0:
            file = open(fileName)
            Profiles = json.load(file)
            file.close()
        else:
            Profiles = {}

        usr = e.get()
        if usr.lower() in Profiles.keys():
            yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,25,client)
        else:
            yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,50,client)

        if len(yourTweets) > 0:
            if usr.lower() in Profiles.keys():
                tweetList.insert(tk.END,"Updating your profile! This may take awhile...")
                window.update()
                Profiles[usr.lower()] = DataGetter.TwitterDataGetter.updateProfile(Profiles[usr.lower()], yourTweets)
                tweetList.insert(tk.END,"Your profile has been updated! You may now press \"Find Matches\"!")
            else:
                tweetList.insert(tk.END,"Creating your profile! This may take awhile...")
                window.update()
                Profiles[usr.lower()] = DataGetter.TwitterDataGetter.generateProfile(usr.lower(), yourTweets)
                tweetList.insert(tk.END,"Your profile has been created! You may now press \"Find Matches\"!")
            with open(fileName, "w") as outfile:
                json.dump(jsons.dump(Profiles),outfile,indent=2)
        else:
            tweetList.insert(tk.END,"No tweets were found! Are you sure you entered the right username?")
        return

    enter = tk.Button(
        text="Find Matches",
        command = e_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    update = tk.Button(
        text="Create/Update Profile",
        command = u_click,
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
    update.grid(row=3, column=3,padx=5,pady=5)
    tweetList.grid(row = 4, column = 1,padx=5,pady=5)

    window.mainloop()

if __name__ == "__main__": main()

