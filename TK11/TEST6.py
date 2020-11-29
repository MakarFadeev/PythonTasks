from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('Позиционирование виджетов')
window.resizable(False, False)

#Виджеты
button10 = Button(text = 'Button 10', bg = 'black', fg = 'white', width = 10)
button10.pack()

#Конец программы
window.mainloop()
