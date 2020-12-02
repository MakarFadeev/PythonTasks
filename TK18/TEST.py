from tkinter import *
import random

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('')
window.resizable(True, True)
window.iconbitmap('alarm.ico')

def open_change_window():
    global newAlarm, change_window
    change_window = Toplevel()
    change_window.title('Изменить')
    change_window.geometry('300x125')
    change_window.resizable(False, False)
    change_window.iconbitmap('alarm.ico')
    newText = Label(change_window, text = 'Введите новое значение будильника')
    newAlarm = Entry(change_window)
    saveIt = Button(change_window, text = 'Сохранить', command = change_alarm)

    newText.pack()
    newAlarm.pack()
    saveIt.pack()

def change_alarm():
    global newAlarm, change_window
    alarmbox.delete(ACTIVE)
    alarmbox.insert(ACTIVE, newAlarm.get())
    change_window.destroy()

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
alarmbox = Listbox(width = 30, height = 10, justify = CENTER)
whatAlarm = Button(text = 'Случайные будильники', command = generate_alarms)
delAlarm = Button(text = 'Удалить будильники', command = delete_alarms)
delThisAlarm = Button(text = 'Удалить выбранный будильник', command = delete_this_alarm)
editThisAlarm = Button(text = 'Изменить будильник', command = open_change_window)

budilnik.pack()
alarmbox.pack()
whatAlarm.pack()
delAlarm.pack()
delThisAlarm.pack()
editThisAlarm.pack()

#Конец программы
window.mainloop()
