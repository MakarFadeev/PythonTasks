print('первая задача: ')
for firstTry in range(7, -6, -2):
    print(firstTry)

"""
print('вторая задача: ')
for firstNumber in range(1, 11):
    for secondNumber in range(1, 11):
        print(firstNumber, ' * ', secondNumber, ' = ', secondNumber*firstNumber)
        print(firstNumber, ' + ', secondNumber, ' = ', secondNumber+firstNumber)
"""
result = 0
result2 = 1

print('вторая задача: ')
for firstNumber in range(1, 11):
    result += firstNumber
    result2 = result2 * firstNumber

print('Сумма всех чисел от 1 до 10:', result)
print('Произведение всех чисел от 1 до 10:', result2)

    
