import time, names, random, tweepy, json, requests, config

from random_username.generate import generate_username

class Profile:
    def __init__(self, name, username, celeb, food, pet, score):
        self.name = name
        self.username = username
        self.celeb = celeb
        self.food = food
        self.pet = pet
        self.score = score

class style:
   YELLOW = '\033[43m'
   END = '\033[0m'

usr = input("Enter Social Media Profile Username: ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

client = tweepy.Client(bearer_token=config.bearer_token)
query = 'from:' + usr + ' -is:retweet'
tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=10)
#tweets is <class 'tweepy.client.Response'>
#tweets.data is <class 'list'>
for tweet in tweets.data:
    #tweet is <class 'tweepy.tweet.Tweet'>
    #tweet.data is <class 'dict'>
    #json.dumps(tweet.data) is <class 'str'> of the tweet.data dict
    print(tweet.text)
    print(tweet.created_at)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




# print("\nHere is your profile summary.")
# You = Profile(names.get_full_name(), usr, "Andrew Tate", "Hawaiian Pizza", "Cats", 3)
# print("Name: " + You.name)
# print("Username: " + You.username)
# print("Favorite Celebrity: " + You.celeb)
# print("Favorite Food: " + You.food)
# print("Favorite Pet: " + You.pet)

# print("\nGathering Profiles...")
# celebs = ["Andrew Tate", "Andrew Tate", "Andrew Tate", "Andrew Tate", "Tony Hawk", "Harry Styles", "Matteo Berrettini", "Nicki Minaj", "Halsey", "Simone Biles"]
# foods = ["Hawaiian Pizza", "Hawaiian Pizza", "Hawaiian Pizza", "Hawaiian Pizza", "Tacos", "Spaghetti", "Steak", "Salad", "Chicken Sandwich", "Corn"]
# pets = ["Cats", "Cats", "Cats", "Cats", "Dogs", "Dogs", "Dogs", "Dogs", "Fish", "Lizards"]
# random.shuffle(celebs)
# random.shuffle(foods)
# random.shuffle(pets)

# Profiles = []

# for i in range(10):
#     score = 0
#     if celebs[i] == You.celeb:
#         score += 1
#     if foods[i] == You.food:
#         score += 1
#     if pets[i] == You.pet:
#         score += 1
#     Profiles.append(Profile(names.get_full_name(), generate_username(1)[0], celebs[i], foods[i], pets[i], score))

# time.sleep(2)
# print(str(len(Profiles)) + " Profiles Found! Generating Results...")
# print()
# time.sleep(2)
# Profiles.sort(key=lambda x: x.score, reverse=True)
# print("Here are your results, sorted by # of shared topics: ")
# print()
# for i in range(10):
#     print("#" + str(i+1))
#     print("Name: " + Profiles[i].name)
#     print("Username: " + Profiles[i].username)
#     if Profiles[i].celeb == You.celeb:
#         print("Favorite Celebrity: " + style.YELLOW + Profiles[i].celeb + style.END)
#     else:
#         print("Favorite Celebrity: " + Profiles[i].celeb)
#     if Profiles[i].food == You.food:
#         print("Favorite Food: " + style.YELLOW + Profiles[i].food + style.END)
#     else:
#         print("Favorite Food: " + Profiles[i].food)
#     if Profiles[i].pet == You.pet:
#         print("Favorite Pet: " + style.YELLOW + Profiles[i].pet + style.END)
#     else:
#         print("Favorite Pet: " + Profiles[i].pet)
#     print("Similarity Score: " + str(Profiles[i].score))
#     print()
# time.sleep(2)
