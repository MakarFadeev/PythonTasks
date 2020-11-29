from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('Позиционирование виджетов')
window.resizable(False, False)

#Виджеты
frame1 = LabelFrame(text = 'Что внутри меня?', width =  300, height = 200)
button10 = Button(frame1, text = 'Button 10', bg = 'black', fg = 'white', width = 10)
frame1.pack(expand = True)
button10.pack()

#Конец программы
window.mainloop()
