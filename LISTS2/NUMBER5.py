n = int(input('Сколько чисел вы хотите ввести? '))
if (n == 0):
    print('0')
else:
    array = []
    printArray = 0
    for i in range(0, n):
        array.append(int(input('Введите число: ')))
        if (i % 2 == 0):
            printArray += array[i]
    print(printArray * array[0])
