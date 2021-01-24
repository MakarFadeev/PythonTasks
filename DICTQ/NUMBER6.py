classmates = {'Петя': 9, 'Вася': 7, 'Ваня': 5, 'Толя': 3, 'Маша': 1, 'Учитель': 11, 'Саша': 0.25}
names = ['Петя', 'Вася', 'Ваня', 'Толя', 'Маша', 'Учитель']
del classmates['Саша']
for name in names:
    if classmates[name] <= 3:
        while classmates[name] <= 3:
            classmates[name] += classmates[name]
    if classmates[name] > 8:
        print(name, ': ', classmates[name])
