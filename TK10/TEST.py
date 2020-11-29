from tkinter import *

#Настройки окна
window = Tk()
window.geometry('400x250')
window.title('Чё на название смотришь?')
window.maxsize(500, 300)
window.minsize(300, 200)
window.resizable(True, True)

#Виджеты
close = Button(text = 'Закрыть программу', width = 20, command = quit)
close.pack(expand = True)

#Конец программы
window.mainloop()
