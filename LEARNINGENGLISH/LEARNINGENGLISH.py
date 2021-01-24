from tkinter import *
from dictionary import words
import random

rus_words = words
eng_words = dict([[v, k] for k, v in words.items()])
cnt = 0

root = Tk()
root.geometry('225x300')
root.resizable(False, False)
root.title('Learning English')

def chooseWord(language):
    global letters, buttons
    if language == 'rus':
        text = ([i for i in rus_words])
        test = random.choice([i for i in rus_words])
        return test
    if language == 'eng':
        text = ([i for i in eng_words])
        test = random.choice([i for i in eng_words])
        return test

def showMenu():
    menu1.pack()
    menu2.pack()

def hideMenu():
    menu1.pack_forget()
    menu2.pack_forget()

def startLevel(language):
    global letters, buttons, rus_words, eng_words, root
       
    hideMenu()
    word = chooseWord(language)
    if language == 'rus':
        letters = None
        buttons = []
        column = 0
        row = 3
        randomLetters = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(25 - len(word))]
        label1 = Label(root, text = rus_words.get(word), font = 'Arial 20')
        label1.grid(columnspan=5, sticky="ew")
        letters = [i for i in word] + randomLetters
        random.shuffle(letters)
        for i in range(len(letters)):
            button = Button(root, text = letters[i], width = 5)
            buttons.append(button)
            buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
            buttons[i].grid(column = column, row = row, sticky = 'ew')
            column += 1
            if column > 4:
                column = 0
                row += 1
                
    if language == 'eng':
        letters = None
        buttons = []
        column = 0
        row = 3
        randomLetters = [random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ') for i in range(33 - len(word))]
        label1 = Label(root, text = eng_words.get(word), font = 'Arial 20')
        label1.grid(columnspan=5, sticky="ew")
        letters = [i for i in word] + randomLetters
        random.shuffle(letters)
        for i in range(len(letters)):
            button = Button(root, text = letters[i], width = 5)
            buttons.append(button)
            buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
            buttons[i].grid(column = column, row = row, sticky = 'ew')
            column += 1
            if column > 4:
                column = 0
                row += 1
    letters = [i for i in word] + randomLetters
    random.shuffle(letters)

    label2 = Label(root, text = '', font = 'Arial 20')
    label2.grid(columnspan=5, sticky="ewsn")
    
    def chooseLetter(button):
        global cnt
        #buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
        if button.cget('text') == word[cnt] and button.cget('bg') != 'green':
            button.config(bg = 'green')
            label2.config(text = label2.cget('text') + word[cnt])
            cnt += 1
        elif button.cget('bg') != 'green':
            for i in buttons:
                i.config(bg = 'SystemButtonFace')
            label2.config(text = '')
            cnt = 0
            if cnt > len(word) - 1:
                cnt = 0
                delete()
                showMenu()

    def delete():
        buttons = []
        label1 = None
        label2 = None

menu1 = Button(text = 'Can you translate?\nENG --> RUS', width = 300, height = 7, command = lambda lang = 'eng': startLevel(lang))
menu2 = Button(text = 'Can you translate?\nRUS --> ENG', width = 300, height = 7, command = lambda lang = 'rus': startLevel(lang))

showMenu()

root.mainloop()
