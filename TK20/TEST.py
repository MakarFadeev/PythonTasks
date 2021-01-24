from tkinter import *
import random
import time

sticks = 20

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('Палочки')
window.maxsize(500, 300)
window.minsize(300, 200)
window.resizable(True, True)

def player():
    global sticks
    delete_sticks = int(entry_sticks.get())
    if delete_sticks > 0 and delete_sticks < 4 and delete_sticks <= sticks:
        sticks -= delete_sticks
        label_sticks.config(text = sticks * '|')
        status.config(text = sticks)
        if sticks == 1:
            status.config(text = 'Вы победили!', fg = 'green')
            button.destroy()
        elif sticks == 0:
            status.config(text = 'Компьютер выиграл!', fg = 'red')
            button.destroy()
        else:
            label_move.config(text = 'Ход компьютера, ожидайте...')
            time.sleep(2)
            computer()

def computer():
    global sticks
    delete_sticks = random.randint(1, 3)
    sticks -= delete_sticks
    label_sticks.config(text = sticks * '|')
    status.config(text = sticks)
    if sticks == 1:
        status.config(text = 'Компьютер выиграл!', fg = 'red')
        button.destroy()
    elif sticks == 0:
        status.config(text = 'Вы победили!', fg = 'green')
        button.destroy()
    else:
        label_move.config(text = 'Введите число от 1 до 3')

#Виджеты
label_move = Label(text = 'Введите число от 1 до 3', font = ('Arial', 15, 'bold'))
entry_sticks = Entry(font = ('Arial', 15, 'bold'))
label_sticks = Label(text = sticks * '|', font = ('Arial', 30, 'bold'))
status = Label(text = sticks, font = ('Arial', 30, 'bold'))
button = Button(text = 'Взять палочки', font = ('Arial', 15, 'bold'), command = player)

label_move.pack()
entry_sticks.pack()
label_sticks.pack()
status.pack()
button.pack()

#Конец программы
window.mainloop()
