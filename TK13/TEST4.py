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
               'чёта я на дне каком-то...', justify = CENTER, relief = RAISED, bd = 10, bg = 'gray39', fg = 'gray12')
label1.grid()

#Конец программы
window.mainloop()
