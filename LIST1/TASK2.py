print('Введите меню (через пробелы)')
menu = input().split(' ')
string = 'test0'
for string in menu:
   if(string[0].isupper() == True):
      print(string)
