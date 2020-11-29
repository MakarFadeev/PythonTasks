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
button13 = Button(frame2, text = 'Кнопочка 4', bg = 'black', fg = 'white', width = 10)
button14 = Button(frame2, text = 'Кнопочка 5', bg = 'black', fg = 'white', width = 10)
button15 = Button(frame2, text = 'Кнопочка 6', bg = 'black', fg = 'white', width = 10)
button16 = Button(frame2, text = 'Кнопочка 7', bg = 'black', fg = 'white', width = 10)
button17 = Button(frame2, text = 'Кнопочка 8', bg = 'black', fg = 'white', width = 10)
button18 = Button(frame2, text = 'Кнопочка 9', bg = 'black', fg = 'white', width = 10)
frame1.pack()
frame2.pack()
frame3.pack()
button10.pack(padx = 10, pady = 10)
button11.pack(padx = 10, pady = 10)
button12.pack(padx = 10, pady = 10)
button13.grid(column = 0, row = 0, padx = 5, pady = 5)
button14.grid(column = 0, row = 1, padx = 5, pady = 5)
button15.grid(column = 1, row = 1, padx = 5, pady = 5)
button16.grid(column = 0, row = 2, padx = 5, pady = 5)
button17.grid(column = 1, row = 2, padx = 5, pady = 5)
button18.grid(column = 0, row = 4, padx = 5, pady = 5)

#Конец программы
window.mainloop()
