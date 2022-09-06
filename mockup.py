import time

usr = input("Enter Social Media Profile:")

print("Welcome " + usr + "! Finding you matches")
matches = ["Angela", "Pamela", "Samantha", "Amanda", "Tamara", "Dale", "Hank", "Bill", "Bobby", "Boomhauer"]
time.sleep(5)
print("Matches found!")
for i in range(0,10):
    print("#" + str(i+1) + " match: " + matches[i])
time.sleep(15)