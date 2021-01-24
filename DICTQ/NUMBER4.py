classmates = {'Петя': 9, 'Вася': 7, 'Ваня': 5, 'Толя': 3, 'Маша': 1, 'Саша': 0.25, 'Учитель': 11}
names = ['Петя', 'Вася', 'Ваня', 'Толя', 'Маша', 'Саша', 'Учитель']
for name in names:
    if classmates[name] <= 3:
        while classmates[name] <= 3:
            classmates[name] += classmates[name]
    print(name, ': ', classmates[name])
