from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('Виджеты и их аргументы')
window.resizable(False, False)

#Виджеты
label1 = Label(text = 'а я то чё? я ничего!')
label1.grid()

#Конец программы
window.mainloop()
