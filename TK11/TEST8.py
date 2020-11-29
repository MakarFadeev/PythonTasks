from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('Позиционирование виджетов')
window.resizable(False, False)

#Виджеты
frame1 = LabelFrame(text = 'Pack', width =  300, height = 200)
frame2 = LabelFrame(text = 'Grid', width =  300, height = 200)
frame3 = LabelFrame(text = 'Place', width =  300, height = 200)
button10 = Button(frame1, text = 'Кнопочка 1', bg = 'black', fg = 'white', width = 10)
button11 = Button(frame1, text = 'Кнопочка 2', bg = 'black', fg = 'white', width = 10)
button12 = Button(frame1, text = 'Кнопочка 3', bg = 'black', fg = 'white', width = 10)
frame1.pack()
frame2.pack()
frame3.pack()
button10.pack(padx = 10, pady = 10)
button11.pack(padx = 10, pady = 10)
button12.pack(padx = 10, pady = 10)

#Конец программы
window.mainloop()
