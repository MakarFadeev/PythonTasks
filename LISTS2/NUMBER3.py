import random
n = int(input('сколько чисел вы хотите получить? '))
array = []
for i in range(0, n):
    array.append(int(random.randint(1, 1000000)))
print(* array)
