from tkinter import *
import random
import time

#Настройки окна
window = Tk()
window.geometry('700x700')
window.title('Деньги и экономия')
window.resizable(True, True)

money = 10000
oilPrice = 60
cottonPrice = 200
goldPrice = 30000
oilHave = 0
cottonHave = 0
goldHave = 0
timeUntilDeath = 360
timeLeft = 0

print('добро пожаловать в "деньги и экономия"! ваша цель - заработать 100 миллионов за 30 лет.')
textOil = 'Цена нефти 60 РублеКоинов за литр'
textCotton = 'Цена хлопка 200 РублеКоинов за килограмм'
textGold = 'Цена золота 30000 РублеКоинов за слиток'
howMoney = 'У вас есть 10000 РублеКоинов'
howManyOilHave = 'У вас есть 0 литров нефти'
howManyCottonHave = 'У вас есть 0 килограмм хлопка'
howManyGoldHave = 'У вас есть 0 слитков золота'

def fBuyOil():
    global money, buyOil, price, notEnoughMoneyOil, oilPrice, oilHave, howMoney, howManyMoney, howManyOilHave
    howMany = int(buyOil.get())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        oilHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyOil.config(text = 'У вас есть ' + str(oilHave) + ' литров нефти') 
        notEnoughMoneyOil.config(text = 'Куплено!', fg = '#007011')
    else:
        notEnoughMoneyOil.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')

def fSellOil():
    global money, sellOil, price, notEnoughMoneyOil, oilPrice, oilHave, howMoney, howManyMoney, howManyOilHave
    howMany = int(sellOil.get())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (howMany <= oilHave and howMany > 0):
        oilHave -= howMany
        money += price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyOil.config(text = 'У вас есть ' + str(oilHave) + ' литров нефти') 
        notEnoughMoneyOil1.config(text = 'Продано!', fg = '#007011')
    else:
        notEnoughMoneyOil1.config(text = 'Недостаточно нефти!', fg = '#ff0000')
        
def fBuyCotton():
    global money, buyCotton, price, notEnoughMoneyCotton, cottonPrice, cottonHave, howMoney, howManyMoney, howManyCottonHave
    howMany = int(buyCotton.get())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        cottonHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyCotton.config(text = 'У вас есть ' + str(cottonHave) + ' килограммов хлопка') 
        notEnoughMoneyCotton.config(text = 'Куплено!', fg = '#007011')
    else:
        notEnoughMoneyCotton.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')

def fSellCotton():
    global money, sellCotton, price, notEnoughMoneyCotton, cottonPrice, cottonHave, howMoney, howManyMoney, howManyCottonHave
    howMany = int(sellCotton.get())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (howMany <= cottonHave and howMany > 0):
        cottonHave -= howMany
        money += price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyCotton.config(text = 'У вас есть ' + str(cottonHave) + ' килограммов хлопка') 
        notEnoughMoneyCotton1.config(text = 'Продано!', fg = '#007011')
    else:
        notEnoughMoneyCotton1.config(text = 'Недостаточно хлопка!', fg = '#ff0000')


def fBuyGold():
    global money, buyGold, price, notEnoughMoneyGold, goldPrice, goldHave, howMoney, howManyMoney, howManyGoldHave
    howMany = int(buyGold.get())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        goldHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyGold.config(text = 'У вас есть ' + str(goldHave) + ' слитков золота') 
        notEnoughMoneyGold.config(text = 'Куплено!', fg = '#007011')
    else:
        notEnoughMoneyGold.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')

def fSellGold():
    global money, sellGold, price, notEnoughMoneyGold, goldPrice, goldHave, howMoney, howManyMoney, howManyGoldHave
    howMany = int(sellGold.get())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (howMany <= goldHave and howMany > 0):
        goldHave -= howMany
        money += price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        howManyMoney.config(text = howMoney)
        howManyGold.config(text = 'У вас есть ' + str(goldHave) + ' слитков золота') 
        notEnoughMoneyGold1.config(text = 'Продано!', fg = '#007011')
    else:
        notEnoughMoneyGold1.config(text = 'Недостаточно золота!', fg = '#ff0000')

def endThisMonth():
    global timeUntilDeath, timeLeft, goldPrice, cottonPrice, oilPrice, whatGoldPrice, whatCottonPrice, whatOilPrice, textOil, textCotton, textGold
    timeUntilDeath -= 1
    timeLeft += 1
    goldPrice += random.randint(-2000, 2000)
    cottonPrice += random.randint(-500, 500)
    oilPrice += random.randint(-100, 100)
    if (goldPrice <= 0):
        goldPrice = 30000
    if (cottonPrice <= 0):
        cottonPrice = 200
    if (oilPrice <= 0):
        oilPrice = 60
    if (goldPrice < 15000):
        goldPrice += 1000
    if (cottonPrice < 70):
        cottonPrice += 100
    if (oilPrice < 20):
        oilPrice += 100
    textOil = 'Цена нефти ' + str(oilPrice) + ' РублеКоинов за литр'
    textCotton = 'Цена хлопка ' + str(cottonPrice) + ' РублеКоинов за килограмм'
    textGold = 'Цена золота ' + str(goldPrice) + ' РублеКоинов за слиток'
    whatOilPrice.config(text = textOil)
    whatCottonPrice.config(text = textCotton)
    whatGoldPrice.config(text = textGold)

#Виджеты
mainLobby = LabelFrame(text = 'Главное меню', width = 100, height = 100)
gameLobby = LabelFrame(mainLobby, text = 'Меню игры', width = 50, height = 100)
gameProcess = LabelFrame(mainLobby, text = 'Игровой процесс', width = 50, height = 50)
settings = LabelFrame(mainLobby, text = 'Настройки', width = 50, height = 50)
#Нефть
oil = LabelFrame(gameLobby, text = 'Нефть')
buyOilText = Label(oil, text = 'Купить нефть')
buyOil = Entry(oil)
buyOilButton = Button(oil, text = 'Купить', command = fBuyOil)
notEnoughMoneyOil = Label(oil, text = '')
sellOilText = Label(oil, text = 'Продать нефть')
sellOil = Entry(oil)
sellOilButton = Button(oil, text = 'Продать', command = fSellOil)
notEnoughMoneyOil1 = Label(oil, text = '')
#Хлопок
cotton = LabelFrame(gameLobby, text = 'Хлопок')
buyCottonText = Label(cotton, text = 'Купить хлопок')
buyCotton = Entry(cotton)
buyCottonButton = Button(cotton, text = 'Купить', command = fBuyCotton)
notEnoughMoneyCotton = Label(cotton, text = '')
sellCottonText = Label(cotton, text = 'Продать хлопок')
sellCotton = Entry(cotton)
sellCottonButton = Button(cotton, text = 'Продать', command = fSellCotton)
notEnoughMoneyCotton1 = Label(cotton, text = '')
#Золото
gold = LabelFrame(gameLobby, text = 'Золото')
buyGoldText = Label(gold, text = 'Купить золото')
buyGold = Entry(gold)
buyGoldButton = Button(gold, text = 'Купить', command = fBuyGold)
notEnoughMoneyGold = Label(gold, text = '')
sellGoldText = Label(gold, text = 'Продать золото')
sellGold = Entry(gold)
sellGoldButton = Button(gold, text = 'Продать', command = fSellGold)
notEnoughMoneyGold1 = Label(gold, text = '')
#Игровой процесс
endMonth = Button(gameProcess, text = 'Закончить месяц', command = endThisMonth)
whatOilPrice = Label(gameProcess, text = textOil)
whatCottonPrice = Label(gameProcess, text = textCotton)
whatGoldPrice = Label(gameProcess, text = textGold)
howManyMoney = Label(gameProcess, text = howMoney)
howManyOil = Label(gameProcess, text = howManyOilHave)
howManyCotton = Label(gameProcess, text = howManyCottonHave)
howManyGold = Label(gameProcess, text = howManyGoldHave)

#test = Button(mainLobby, width = 10)

mainLobby.pack()
gameLobby.grid(column = 1, row = 0, padx = 10, pady = 10, rowspan = 2)
gameProcess.grid(column = 0, row = 0, padx = 10, pady = 10)
settings.grid(column = 0, row = 1, padx = 10, pady = 10)
oil.grid(column = 0, row = 0, padx = 10, pady = 10)
buyOilText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyOil.grid(column = 1, row = 0, padx = 5, pady = 5)
buyOilButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyOil.grid(column = 0, row = 1, padx = 5, pady = 5)
sellOilText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellOil.grid(column = 1, row = 2, padx = 5, pady = 5)
sellOilButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyOil1.grid(column = 0, row = 4, padx = 5, pady = 5)
cotton.grid(column = 0, row = 1, padx = 10, pady = 10)
buyCottonText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyCotton.grid(column = 1, row = 0, padx = 5, pady = 5)
buyCottonButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyCotton.grid(column = 0, row = 1, padx = 5, pady = 5)
sellCottonText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellCotton.grid(column = 1, row = 2, padx = 5, pady = 5)
sellCottonButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyCotton1.grid(column = 0, row = 4, padx = 5, pady = 5)
gold.grid(column = 0, row = 2, padx = 10, pady = 10)
buyGoldText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyGold.grid(column = 1, row = 0, padx = 5, pady = 5)
buyGoldButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyGold.grid(column = 0, row = 1, padx = 5, pady = 5)
sellGoldText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellGold.grid(column = 1, row = 2, padx = 5, pady = 5)
sellGoldButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyGold1.grid(column = 0, row = 4, padx = 5, pady = 5)
endMonth.grid(column = 0, row = 0, padx = 5, pady = 5)
whatOilPrice.grid(column = 0, row = 1, padx = 5, pady = 5)
whatCottonPrice.grid(column = 0, row = 2, padx = 5, pady = 5)
whatGoldPrice.grid(column = 0, row = 3, padx = 5, pady = 5)
howManyMoney.grid(column = 0, row = 4, padx = 5, pady = 5)
howManyOil.grid(column = 0, row = 5, padx = 5, pady = 5)
howManyCotton.grid(column = 0, row = 6, padx = 5, pady = 5)
howManyGold.grid(column = 0, row = 7, padx = 5, pady = 5)
#test.grid(column = 2, row = 2, padx = 10, pady = 10)

#Конец программы
window.mainloop()
