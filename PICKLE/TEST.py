with open('poems.txt', 'w') as myFile:
    myFile.write('Hello, Python!')

with open('poems.txt', 'r') as myFile:
    info = myFile.readlines()
    #myFile.seek(7)
    #info = myFile.read(6)
    print(info)
