from tkinter import *
import random

root = Tk()
root.title('Виселица')

canvas = Canvas(root, width = 600, height = 600)

canvas.pack()

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 33, fill = 'white', outline = 'blue')
            x += 33
        y += 33

print('Привет! Давай поиграем! Один из игроков загадывает слово — пишет на бумаге первую и последнюю букву слова и отмечает места для остальных букв, например чертами. Также рисуется виселица с петлёй. Второй игрок предлагает букву, которая может входить в это слово. Если такая буква есть в слове, то первый игрок пишет её над соответствующими этой букве чертами — столько раз, сколько она встречается в слове. Если такой буквы нет, то к виселице добавляется круг в петле, изображающий голову. Второй игрок продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. За каждый неправильный ответ первый игрок добавляет одну часть туловища к виселице. Если туловище в виселице нарисовано полностью, то отгадывающий игрок проигрывает, считается повешенным. Если игроку удаётся угадать слово, он выигрывает.')
slova = ['страница', 'виселица', 'смартфон', 'креветка', 'мегагерц', 'маргарин']

def arr():
    but()
    word = random.choice(slova)
    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text = word[0], fill = 'purple', font = ('Helvetica', '18'))
    a1 = canvas.create_text(315, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a2 = canvas.create_text(347, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a3 = canvas.create_text(380, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a4 = canvas.create_text(412, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a5 = canvas.create_text(444, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a6 = canvas.create_text(477, 40, text = '_', fill = 'purple', font = ('Helvetica', '18'))
    a6 = canvas.create_text(510, 40, text = word[-1], fill = 'purple', font = ('Helvetica', '18'))
    list1 = [1, 2, 3, 4, 5, 6]
    alfabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    er = []
    win = []
    
    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]
        if v in wor:
            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = '1'
            
            def kord():

                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1
            
            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text = wo[ind], font = ('Helvetica', '18'))
            btn[key]['bg'] = 'green'
            if not v in wor:
                btn[key]['state'] = 'disabled'
            if v in wor:
                win.append(v)
                ind2 = wor.index(v)
                b2 = list1[ind2]
                x1,y1=kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win)==6:
                canvas.create_text(150, 150, text="Ты победил", fill="purple", font=("Helvetica", "18"))
                for i in alfabet:
                    btn[i]['state'] = 'disabled'
        else:
            er.append(v)
            btn[key]['bg'] = 'red'
            btn[key]['state'] = 'disabled'

            if len(er) == 1:
                golova()
            elif len(er) == 2:
                telo()
            elif len(er) == 3:
                rukaL()
            elif len(er) == 4:
                rukaP()
            elif len(er) == 5:
                nogaL()
            elif len(er) == 6:
                nogaP()
                end()
            root.update()
            
    btn = {}
    
    def gen(x, y, u):
        btn[u] = Button(root, text = u, width = 3, height = 1, command = lambda: a(u))
        btn[u].place(x = str(x), y = str(y))
    x = 265
    y = 110
    for i in alfabet[0:8]:
        gen(x, y, i)
        x += 33
    x = 265
    y = 137
    for i in alfabet[8:16]:
        gen(x, y, i)
        x += 33
    x = 265
    y = 164
    for i in alfabet[16:24]:
        gen(x, y, i)
        x += 33
    x = 265
    y = 191
    for i in alfabet[24:33]:
        gen(x, y, i)
        x += 33


    
    def golova():
        canvas.create_oval(79, 59, 120, 80, width = 4, fill = 'white')
        root.update()

    def telo():
        canvas.create_line(100, 80, 100, 200, width = 4)
        root.update()

    def rukaP():
        canvas.create_line(100, 80, 145, 100, width = 4)
        root.update()

    def rukaL():
        canvas.create_line(100, 80, 45, 100, width = 4)
        root.update()

    def nogaL():
        canvas.create_line(100, 200, 45, 300, width = 4)
        root.update()

    def nogaP():
        canvas.create_line(100, 200, 145, 300, width = 4)
        root.update()
    

    def end():
        canvas.create_text(150, 150, text = 'Вы проиграли!', fill = 'red', font = ('Helvetica', '18'))
        for i in alfabet:
            btn[i]['state'] = 'disabled'
    
btn01 = Button(root, text = 'Начать', width = 10, bg = 'red', command = lambda: arr())
btn01.place(x = 100, y = 300)

root.mainloop()
