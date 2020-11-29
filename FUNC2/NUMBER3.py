def smallest(a, b, c):
    if (a < b):
        if (a < c):
            print(a)
        if (c < a):
            print(c)
    elif (b < a):
        if (b < c):
            print(b)
        if (c < b):
            print(c)
    elif (c < a):
        if (c < b):
            print(c)
        if (b < c):
            print(c)
    else:
        print('Тут нет самого маленького числа!')
smallest(2, 2, 3)
    
