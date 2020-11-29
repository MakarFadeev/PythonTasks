from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('Виджеты и их аргументы')
window.resizable(False, False)

#Виджеты
label1 = Label(text = 'а я то чё? я ничего!\n'
               'а я и пониже писать умею!\n'
               'и ещё ниже...\n'
               'чёта я на дне каком-то...', justify = CENTER, relief = RAISED, bd = 10, bg = '#9e9e9e', fg = '#474747', font = 'Veranda 10 italic')
label2 = LabelFrame(bg = 'gray99', fg = 'gray99')
button1 = Button(label2, text = 'ОТМЕНА', bg = 'OrangeRed2', fg = 'gray10')
button2 = Button(label2, text = 'А я зелёненький)', bg = 'green2', fg = 'gray10')
label1.grid()
label2.grid()
button1.grid(column = 0, row = 0, padx = 5, pady = 10)
button2.grid(column = 1, row = 0, padx = 5, pady = 10)

#Конец программы
window.mainloop()
