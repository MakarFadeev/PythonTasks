string = input('Введите строку: ')
printString = ' '
for i in range(0, len(string)):
    if (string[i] <= 'и'):
        printString = printString + string[i]
print(printString)
