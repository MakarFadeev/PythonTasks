numbers = int(input('сколько чисел вы хотите ввести? '))
n = int(input('введите число (любое!): ')) - 1
array = []
for i in range(0, numbers):
    array.append(int(input('введите число: ')))
print(array[n] ** n)
