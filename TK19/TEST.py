from tkinter import *

#Настройки окна
window = Tk()
window.geometry('550x300')
window.title('color picker')
window.resizable(False, False)

#Виджеты
frame_RGB = LabelFrame(height = 250, width = 250, text = 'Выберите цвета')
frame_color = LabelFrame(height = 250, width = 250, text = 'Полученный цвет')
label_color = Label(frame_color, font = ('Arial', 15, 'bold'), height = 8, width = 16)
red_text = Label(frame_RGB, text = 'Красный', fg = 'red')
red_scale = Scale(frame_RGB, to = 255, orient = HORIZONTAL, width = 20, length = 200)

frame_RGB.place(x = 10, y = 10)
frame_color.place(x = 270, y = 10)
label_color.place(x = 10, y = 10)
red_scale.place(x = 10, y = 30)
red_text.place(x = 10, y = 10)

#Конец программы
window.mainloop()
