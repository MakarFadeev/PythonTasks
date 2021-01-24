from tkinter import *

root = Tk()
root.geometry('225x230')
root.resizable(False, False)
root.title('Learning English')

def showMenu():
    menu1.pack()
    menu2.pack()

def hideMenu():
    menu1.pack_forget()
    menu2.pack_forget()

menu1 = Button(text = 'Can you translate?\nENG --> RUS', width = 300, height = 7)
menu2 = Button(text = 'Can you translate?\nRUS --> ENG', width = 300, height = 7)

showMenu()

root.mainloop()
