
import time, tweepy, config
import tkinter as tk
from simplemagic import sm
import DataGetter
import meaningcloud
import profile
import json, jsons


def main():

    client = tweepy.Client(bearer_token=config.bearer_token)

    getdata = input("yes to update/create profiles: ")
    if (getdata == "yes"):
        DataGetter.TwitterDataGetter.get_data(10,client)

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

    def u_click():
        tweetList.delete(0,tk.END)

        fileName = "testDataBoogaloo.json"
        file = open(fileName)
        Profiles = json.load(file)
        file.close()

        usr = e.get()
        yourTweets = DataGetter.TwitterDataGetter.get_users_tweets(usr,10,client)

        if usr.lower() in Profiles.keys():
            tweetList.insert(tk.END,"Updating your profile! This may take awhile...")
            Profiles[usr.lower()] = DataGetter.TwitterDataGetter.updateProfile(Profiles[usr.lower()], yourTweets)
            tweetList.insert(tk.END,"Your profile has been updated! Press \"Enter\" to find matches!")
        else:
            tweetList.insert(tk.END,"Creating your profile! This may take awhile...")
            Profiles[usr.lower()] = DataGetter.TwitterDataGetter.generateProfile(usr.lower(), yourTweets)
            tweetList.insert(tk.END,"Your profile has been created! Press \"Enter\" to find matches!")
        
        with open(fileName, "w") as outfile:
            json.dump(jsons.dump(Profiles),outfile,indent=2)
        return


    def e_click():
        tweetList.delete(0,tk.END)

        fileName = "testDataBoogaloo.json"
        file = open(fileName)
        Profiles = json.load(file)
        file.close()

        usr = e.get()
        numInput = output.get()

        if numInput != '':
            numberofmatches = int(numInput)
        else:
            numberofmatches = 0
            
        
        if usr.lower() in Profiles.keys():
            yourProfile = Profiles[usr.lower()]

            lengthsim = {}
            for pot in Profiles:
                lengthsim.update({Profiles[pot]['username']: Profiles[pot]['avglen'] - yourProfile['avglen']})
            matchesmade = dict(sorted(lengthsim.items(), key=lambda item: abs(item[1])))
            count = 0
            tweetList.insert(tk.END,"Your Average Tweet Length: " + str(round(yourProfile['avglen'],1)))
            tweetList.insert(tk.END,"")
            for match in matchesmade:
                if count == numberofmatches:
                    break
                if match != yourProfile['username']:
                    tweetList.insert(tk.END,"Twitter handle: " + str(match))
                    tweetList.insert(tk.END,"Average Tweet Length: " + str(round(matchesmade[match] + yourProfile['avglen'],1)))
                    tweetList.insert(tk.END,"Closeness to your length: " + str(round(matchesmade[match],1)))
                    tweetList.insert(tk.END,"")
                    count +=1
        else:
            tweetList.insert(tk.END,"Your twitter handle isn't in the database! Press \"Update\" to add yourself to it!")
        return

    enter = tk.Button(
        text="Enter",
        command = e_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    update = tk.Button(
        text="Update",
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

