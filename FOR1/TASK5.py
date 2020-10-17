string = input('введите строку: ')
result = ''

print('Первое задание: ')
for i in range(0, len(string)):
    if (string[i]=='а'):
        break
    result = result + string[i]
if (result == string):
    print('В этом слове не найдено букв "а"')
print(result)

print('Второе задание: ')
delete = string.rfind('а')
if (delete == -1):
    print('В этом слове не найдено букв "а" ')
print(string[:delete])
