from tkinter import *
from tkinter import filedialog

#Настройки окна
window = Tk()
window.geometry('400x500')
window.title('Список дел')
window.resizable(False, False)

whatNumber = 1
def add():
    global whatNumber
    whatNumber = str(whatNumber)
    text = whatNumber + '.' + what.get() + '   ' + when.get() + '\n'
    todolist.insert(END, text)
    what.delete(0, END)
    when.delete(0, END)
    whatNumber = int(whatNumber)
    whatNumber += 1

def clear():
    global whatNumber
    todolist.delete(0.0, END)
    whatNumber = 1

def save():
   text = todolist.get(0.0, END)
   file = filedialog.asksaveasfile(title = 'Сохранить список', filetypes = (('txt files', '*.txt'), ('all files', '*.*')))
   if file:
       file.write(text)

def load():
    todolist.delete(0.0, END)
    file = filedialog.askopenfile(title = 'Выберите файл', filetypes = (('txt files', '*.txt'), ('all files', '*.*')))
    text = file.read()
    todolist.insert(END, text)

#Виджеты
deal = LabelFrame(text = 'Записать важное дело')
whatText = Label(deal, text = 'Какое дело')
what = Entry(deal)
whenText = Label(deal, text = 'Когда нужно сделать')
when = Entry(deal)
doit = Button(deal, text = 'Добавить новое важное дело', command = add)
deleting = Button(deal, text = 'Удалить все записи', command = clear)
saveit = Button(deal, text = 'Сохранить', command = save)
loadit = Button(deal, text = 'Загрузить', command = load)
todolist = Text(width = 35)

deal.pack()
whatText.pack()
what.pack()
whenText.pack()
when.pack()
doit.pack()
deleting.pack()
saveit.pack()
loadit.pack()
todolist.pack()

#Конец программы
window.mainloop()
