array = []
n = int(input('Сколько чисел Вы хотите ввести? '))
for i in range(0, n):
    array.append(int(input('Введите число: ')))
print('Максимальное число: ', max(array))
print('Минимальное число: ', min(array))
print('Разница между максимальным и минимальным числом: ', max(array) - min(array))
