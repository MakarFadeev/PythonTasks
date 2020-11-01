n = int(input('Сколько символов вы хотите ввести (максимум - 10)? '))
array = []
for i in range(0, n):
    array.append(input('Введите символ: '))
print(array[0])
if (n % 2 == 0):
    print(array[int(n / 2)])
else:
    print(array[int(n / 2 + 0.5)])
print(array[n - 1])
