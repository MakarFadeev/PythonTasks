film = input('Введите название фильма: ')
name = input('Введите название кинотеатра: ')
time = input('Введите, во сколько начнётся фильм: ')
yay = lambda film, name, time: 'Билет на " ' + film + ' " в "' + name + '" на' + time + 'забронирован'
print(yay(film, name, time))
