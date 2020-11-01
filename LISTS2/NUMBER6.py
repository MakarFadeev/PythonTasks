n = int(input('Сколько чисел вы хотите ввести? '))
array = []
for i in range(0, n):
    array.append(input('Введите число: '))
    if (i != 0):
        if (array[i] >= array[i - 1]):
            print('НЕТ')
            break
    if (i == n - 1):
        print('ДА')
        
        
