from tkinter import *
from tkinter import messagebox

#Настройки окна
window = Tk()
window.geometry('550x300')
window.title('Решатель примеров')
window.resizable(True, True)

def equate():
    try:
        solution = eval(equation.get())
        messagebox.showinfo('Подождите', 'Программа пьёт чай, подождите пару часиков')
    except SyntaxError:
        messagebox.showwarning('Что это?', 'Садись, [ИМЯ ПОЛЬЗОВАТЕЛЯ], 2! перепроверяй пример!')
    except NameError:
        messagebox.showerror('Ты чаво тваришь...', 'Что ты там понаписал такого???')
    except ZeroDivisionError:
        messagebox.showwarning('Серьёзно?', 'Я твой пример умножу на ноль!')

#Виджеты
root = LabelFrame(text = 'Сосисочки')
frame = Frame(root)
label = Label(root, text = 'Введите математическое выражение из чисел и знаков \n+  -  *  /  //  **')
equation = Entry(root, width = 75)
button = Button(root, text = 'Решить!', width = 50, command = equate)

root.pack()
frame.grid(column = 0, row = 0, padx = 25, pady = 25)
label.grid(column = 0, row = 1, padx = 25, pady = 25)
equation.grid(column = 0, row = 2, padx = 25, pady = 25)
button.grid(column = 0, row = 3, padx = 25, pady = 25)
equation.focus()
#Конец программы
window.mainloop()
