allClassmates = int(input('Сколько учеников в Вашем классе? '))
classmates = []
for i in range(0, allClassmates):
    classmates.append(input('Введите фамилию ученика: '))
classmates.sort()
print(* classmates)
