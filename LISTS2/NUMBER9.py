howMany = int(input('Сколько чисел вы хотите ввести? '))
array = []
better = 9999999999999
betterLength = 99999999999999
n = int(input('Введите главное число: '))
for i in range(0, howMany):
    array.append(int(input('Введите число: ')))
    if (array[i] > n):
        if (array[i] - n < betterLength):
            better = array[i]
            betterLength = array[i] - n
    if (array[i] < n):
        if (n - array[i] < betterLength):
            better = array[i]
            betterLength = n - array[i]
    if (array[i] == n):
        better = array[i]
        betterLength = n - array[i]
print('Самое близкое число: ', better)


