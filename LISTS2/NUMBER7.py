listAlready = []
list1 = input('Введите символы: ')
list2 = input('Введите ещё символов: ')
lenList1 = len(list1)
lenList2 = len(list2)
for i in range(0, lenList1):
    for j in range(0, lenList2):
        if (list1[i] in list2[j]):
            if (list1[i] not in listAlready):
                print(list1[i])
                listAlready.append(list1[i])


