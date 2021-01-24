from tkinter import *

#Настройки окна
window = Tk()
window.geometry('550x300')
window.title('color picker')
window.resizable(False, False)

def color_generate(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    label_color.config(bg = color, text = color)

#Виджеты
frame_RGB = LabelFrame(height = 250, width = 250, text = 'Выберите цвета')
frame_color = LabelFrame(height = 250, width = 250, text = 'Полученный цвет')
label_color = Label(frame_color, font = ('Arial', 15, 'bold'), height = 8, width = 16)
red_text = Label(frame_RGB, text = 'Красный', fg = 'red')
red_scale = Scale(frame_RGB, to = 255, orient = HORIZONTAL, width = 20, length = 200, activebackground = 'red', command = color_generate)
green_text = Label(frame_RGB, text = 'Зелёный', fg = 'green')
green_scale = Scale(frame_RGB, to = 255, orient = HORIZONTAL, width = 20, length = 200, activebackground = 'green', command = color_generate)
blue_text = Label(frame_RGB, text = 'Синий', fg = 'blue')
blue_scale = Scale(frame_RGB, to = 255, orient = HORIZONTAL, width = 20, length = 200, activebackground = 'blue', command = color_generate)

frame_RGB.place(x = 10, y = 10)
frame_color.place(x = 270, y = 10)
label_color.place(x = 10, y = 10)
red_scale.place(x = 10, y = 30)
red_text.place(x = 10, y = 10)
green_scale.place(x = 10, y = 100)
green_text.place(x = 10, y = 80)
blue_scale.place(x = 10, y = 170)
blue_text.place(x = 10, y = 150)

#Конец программы
window.mainloop()
