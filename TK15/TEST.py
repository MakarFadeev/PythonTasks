from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x300')
window.title('Ввод-вывод данных')
window.resizable(False, False)
smallLetter = False
bigLetter = False
number = False
nice = False
def show():
    global smallLetter
    global bigLetter
    global number
    global nice
    password = inputbox.get()
    for i in range(len(password)):
        if (password[i].isupper()):
            bigLetter = True
        elif (password[i].islower()):
            smallLetter = True
        elif (password[i].isdigit()):
            number = True
        elif (number and bigLetter and smallLetter):
            nice = True
    if (len(password) < 10):
        if (not smallLetter and bigLetter and number):
            label2.config(text = 'Не хватает строчных букв!', fg = 'red')
        elif (not bigLetter and smallLetter and number):
            label2.config(text = 'Не хватает заглавных букв!', fg = 'red')
        elif (not number and bigLetter and smallLetter):
            label2.config(text = 'Не хватает цифр!', fg = 'red')
        else:
            label2.config(text = 'Пароль не подходит!', fg = 'red')
    elif (nice and len(password) >= 10):
        label2.config(text = 'Пароль подходит!', fg = 'green')
def theme():
    passwordbox.config(bg = '#353535', fg = 'white')
    label1.config(bg = '#353535', fg = 'white')
    label2.config(bg = '#353535')
    showbutton.config(bg = '#535353', fg = 'white')
    themebutton.config(bg = '#535353', fg = 'white', state = DISABLED)
    window.config(bg = '#353535')
    
#Виджеты
passwordbox = LabelFrame(text = 'Пароль')
label1 = Label(passwordbox, text = 'Введите пароль:', fg = '#000000', width = 20, height = 1)
inputbox = Entry(passwordbox, width = 20, show = '*', justify = CENTER, bg = '#000000', fg = '#ffffff')
label2 = Label(passwordbox, fg = '#000000', width = 30, height = 1)
showbutton = Button(passwordbox, text = 'Проверить пароль', command = show)
themebutton = Button(passwordbox, text = 'Сменить тему', command = theme)

passwordbox.pack()
label1.pack()
inputbox.pack()
label2.pack()
showbutton.pack()
themebutton.pack()

#Конец программы
window.mainloop()
