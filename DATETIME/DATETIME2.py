import datetime
birthdayyear = int(input('Введите год рождения: '))
birthdaymonth = int(input('Введите месяц рождения: '))
birthdayday = int(input('Введите день рождения: '))
birthday = datetime.datetime(birthdayyear, birthdaymonth, birthdayday)
print('с момента вашего рождения прошло ', datetime.datetime.today() - birthday)
