from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('Позиционирование виджетов')
window.resizable(False, False)

#Виджеты
frame1 = LabelFrame(text = 'Pack', width = 300, height = 100)
frame2 = LabelFrame(text = 'Grid', width = 300, height = 100)
frame3 = LabelFrame(text = 'Place', width = 300, height = 100)
frame1.pack()
frame2.pack()
frame3.pack()

#Конец программы
window.mainloop()
