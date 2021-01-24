import pickle
import random

myList = []
summa = 0
for i in range(10):
    myList.append(random.randint(1, 100000))

with open('nums', 'wb') as myFile:
    #info = myFile.readlines()
    #myFile.seek(7)
    #info = myFile.read(6)
    #print(info)
    pickle.dump(myList, myFile)

with open('nums', 'rb') as myFile:
    #myFile.write('Hello, Python!')
    #pass
    loadList = pickle.load(myFile)

print(sum(loadList))
