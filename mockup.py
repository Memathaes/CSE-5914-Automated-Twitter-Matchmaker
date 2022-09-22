import time, tweepy, config
import tkinter as tk
from simplemagic import sm
import DataGetter

def main():

    client = tweepy.Client(bearer_token=config.bearer_token)
    #tweets = DataGetter.TwitterDataGetter.get_Data("katyperry",10,client)

    matches = []
    maj = sm()

    ppl = maj.find("Columbus")

    print(ppl)

    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    greeting = tk.Label(text="Mockup UI")

    #greeting.pack()
    greeting.grid(row=0,column=1)

    label1 = tk.Label(text="Enter Social Media Profile:")
    e = tk.Entry()


    label2 = tk.Label(text="Matches:")
    output = tk.Entry()

    tweetList = tk.Listbox(width=150)

    def e_click():
        user = e.get()
        matches = DataGetter.TwitterDataGetter.get_data(user,10,client)
        for match in matches:
            tweetList.insert(tk.END,match)
            for tweet in matches[match]:
                tweetList.insert(tk.END,tweet)
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

    # usr = input("Enter Social Media Profile:")

    # print("Welcome " + usr + "! Finding you matches")
    # matches = ["Angela", "Pamela", "Samantha", "Amanda", "Tamara", "Dale", "Hank", "Bill", "Bobby", "Boomhauer"]
    # time.sleep(5)
    # print("Matches found!")
    # for i in range(0,10):
    #     print("#" + str(i+1) + " match: " + matches[i])
    # time.sleep(15)

if __name__ == "__main__": main()