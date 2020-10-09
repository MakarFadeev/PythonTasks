friends = ['TEST']
friends = input('Введите рост друзей (через пробел)').split(' ')
string = 'test'
repeat = 0
for repeat in range(len(friends) - 1):
   if(int(friends[repeat])>int(friends[repeat + 1])):
       print(friends[repeat])

