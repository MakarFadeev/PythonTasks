import datetime
whatyear = int(input('Введите год: '))
month = 1
for month in range(1, 13):
    whatyear0 = datetime.date(whatyear, month, 13)
    if (whatyear0.weekday() == 4):
        print('НАЙДЕНА ПЯТНИЦА 13!!! ДАТА: ', whatyear0)

