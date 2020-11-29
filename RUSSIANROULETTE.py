import random

allPlayers = int(input('Введите количество игроков: '))
n = allPlayers * 2

players = []
marbles = []
for i in range(n):
    marbles.append('green')
marbles[random.randint(0, n - 1)] = 'white'
for i in range(allPlayers):
    print('Введите имя игрока #', i + 1, ': ')
    players.append(input())

print('Добро пожаловать в игру “Русская рулетка”!')
print('Правила игры: Из мешка с несколькими зелеными шариками и одним белым каждый игрок по очереди достает по одному шарику. Если достался зеленый шарик - игра идет дальше, если кому-нибудь из игроков достался белый, то игра заканчивается.')
print('Удачи!')

taken = 0
current_player = 0

while(taken <  n):
    print('Очередь игрокa', players[current_player], '!')
    print('Нажите Enter, чтобы достать шарик...')
    test = input()
    if (marbles[taken] == 'white'):
        print('Игра закончена! игрок', players[current_player], 'не выжил!')
        break
    if (marbles[taken] == 'green'):
        print('Фух, повезло! Игрок', players[current_player], 'достал зеленый шарик!')
    current_player = current_player + 1
    taken = taken + 1
    if (current_player == allPlayers):
       current_player = 0
    
