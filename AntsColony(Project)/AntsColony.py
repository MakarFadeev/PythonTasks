from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('Ants Colony')
window.resizable(True, True)

def goUp():
    pass

def goDown():
    pass

def goRight():
    pass

def goLeft():
    pass

#Виджеты
thisGame = LabelFrame(text = 'Игра')
labelGame = Label(thisGame, text = 'Вы играете в \nAnts Colony')
controls = LabelFrame(thisGame, text = 'Управление')
pust = Label(controls, text = '')
up = Button(controls, text = '▲', command = goUp)
right = Button(controls, text = '▶', command = goRight)
left = Button(controls, text = '◀', command = goLeft)
down = Button(controls, text = ' ▼', command = goDown)

thisGame.pack()
labelGame.grid(column = 0, row = 0, padx = 10, pady = 10)
controls.grid(column = 0, row = 1, padx = 10, pady = 10)
pust.grid(column = 0, row = 0, padx = 5, pady = 5)
up.grid(column = 1, row = 0, padx = 5, pady = 5)
left.grid(column = 0, row = 1, padx = 5, pady = 5)
down.grid(column = 1, row = 1, padx = 5, pady = 5)
right.grid(column = 2, row = 1, padx = 5, pady = 5)

#Конец программы
window.mainloop()
