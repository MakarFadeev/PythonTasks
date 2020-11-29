from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x300')
window.title('Ввод-вывод данных')
window.resizable(False, False)
def show():
    outputbox.delete(0, END)
    password = inputbox.get()
    outputbox.insert(0, password)

#Виджеты
passwordbox = LabelFrame(text = 'Пароль')
label1 = Label(passwordbox, text = 'Введите пароль:', fg = '#000000', width = 20, height = 1)
inputbox = Entry(passwordbox, width = 20, show = '*', justify = CENTER, bg = '#000000', fg = '#ffffff')
label2 = Label(passwordbox, text = 'Ваш пароль:', fg = '#000000', width = 20, height = 1)
outputbox = Entry(passwordbox, width = 20, justify = CENTER)
showbutton = Button(passwordbox, text = 'Показать', command = show)

passwordbox.pack()
label1.pack()
inputbox.pack()
label2.pack()
outputbox.pack()
showbutton.pack()

#Конец программы
window.mainloop()
