total = 0
minus = 0
plus = 0
zero = 0
for i in range(7):
    x = int(input('Введите число: '))
    total = total + x
    if (x == 0):
        zero = zero + 1
    if (x < 0):
        minus = minus + 1
    if (x > 0):
        plus = plus + 1
print('Сумма: ', total)
print('Положительных чисел: ', plus)
print('Нулей: ', zero)
print('Отрицательных чисел: ', minus)
