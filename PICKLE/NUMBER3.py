with open('poems.txt', 'w') as myFile:
    myFile.write(' Людей неинтересных в мире нет.\n Их судьбы — как истории планет.\n У каждой все особое, свое,\n и нет планет, похожих на нее.')

with open('poems.txt', 'r') as myFile:
    #info = myFile.readlines()
    #myFile.seek(7)
    info = myFile.read()
    print(info)
