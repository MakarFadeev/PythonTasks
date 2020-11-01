listAlready = []
list1 = input('Введите символы: ')
list2 = input('Введите ещё символов: ')
for char1 in list1:
    for char2 in list2:
        if (char1 in char2):
            if (char1 not in listAlready):
                print(char1)
                listAlready.append(char1)


