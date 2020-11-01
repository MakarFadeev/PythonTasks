n = int(input('сколько чисел вы хотите ввести? '))
array = []
printArray = []
for i in range(0, n):
    array.append(int(input('Введите число: ')))
    if (array[i] % 2 != 0):
        printArray.append(array[i])
print(* printArray)
