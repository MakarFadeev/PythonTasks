from tkinter import *
import random

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('')
window.resizable(True, True)

def generate_alarms():
    alarms = []
    a = 0
    b = 5
    for i in range(10):
        fullRandom = random.randint(a, b)
        if (fullRandom > 9):
            alarms.append('7:' + str(fullRandom))
            a += 5
            b += 5
        else:
            alarms.append('7:0' + str(fullRandom))
            a += 5
            b += 5
    alarmbox.insert(END, *alarms)

def delete_alarms():
    alarmbox.delete(0, END)

def delete_this_alarm():
    indexes = alarmbox.curselection()
    indexes = indexes[::-1]
    for index in indexes:
        alarmbox.delete(index)

#Виджеты
budilnik = Label(text = 'Будильник')
alarmbox = Listbox(width = 30, height = 10, justify = CENTER, selectmode = MULTIPLE)
whatAlarm = Button(text = 'Случайные будильники', command = generate_alarms)
delAlarm = Button(text = 'Удалить будильники', command = delete_alarms)
delThisAlarm = Button(text = 'Удалить выбранный будильник', command = delete_this_alarm)

budilnik.pack()
alarmbox.pack()
whatAlarm.pack()
delAlarm.pack()
delThisAlarm.pack()

#Конец программы
window.mainloop()
