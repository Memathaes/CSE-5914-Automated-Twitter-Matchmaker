import json
from abc import ABC

class sm:
    def find(self, usr):
        f = open('testdata.json', 'r')

        output = []
        td = json.load(f)
        num = 0

        #print(td["person1"]["City"])

        for person in td :
            if (td[person]["City"] == str(usr)):
                num+=1
                output.append(td[person])
                print("find")

        f.close

        #print("test")

        return output