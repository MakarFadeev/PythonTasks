from tkinter import *

#Настройки окна
window = Tk()
window.geometry('200x400')
window.title('Rainbow')
window.resizable(False, False)

#Переменные и функции
codes = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#000080', '#4B0082']
colors = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]

def change_text(index):
    color_name.config(text = colors[index])
    color_code.config(text = codes[index])
    

#Виджеты
color_name = Label(font = 'Arial, 14', bg = '#ffffff', width = 20, height = 2)
color_code = Label(font = 'Arial, 14', bg = '#ffffff', width = 20, height = 2)

color_name.pack()
color_code.pack()
for i in range(0, 7):
    button = Button(width = 25, height = 2, bg = codes[i], command = lambda index = i: change_text(index))
    button.pack()

#Конец программы
window.mainloop()
