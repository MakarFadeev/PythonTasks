import random

endThis = False

def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали!'
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Быки ')
        elif guess[i] in secretNum:
            clue.append('Коровы ')
    if len(clue) == 0:
        return 'В этом числе нет ничего!'
    clue.sort()
    return ''.join(clue)
    
def isOnlyDigits(num):
    if num == '':
        return False
        for i in '1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def playAgain():
     print('Хочешь поиграть еще (да или нет)?')
     return input().lower().startswith('да')
    
numDigits = 3
maxGuess = 10
print('Я задумал %s-значное число. Попробуйте угадать его.' % (numDigits))
print('вот некоторые подсказки:')
print('когда я говорю: это означает:')
print('Быки - одна цифра правильная и в правильном положении.')
print('Коровы - одна цифра является правильным, но в неправильном положении.')
print('В этом числе нет ничего – нет правильных цифр.')
while True:
    secretNum = getSecretNum(numDigits)
    print('Я задумал %s-значное число. Попробуйте угадать его.' % (numDigits))
    numGuesses = 1
    while numGuesses <= maxGuess:
        guess = ''
        if endThis:
            endThis = False
            break
        while len(guess) != numDigits or not isOnlyDigits(guess):
            print('У тебя %s попытка' % (numGuesses))
            guess = input()
            clue = getClues(guess, secretNum)
            print(clue)
            numGuesses += 1
            if guess == secretNum:
                endThis = True
                break
            if numGuesses > maxGuess:
                print(' У вас закончились попытки. Ответ был %s.' % (secretNum))
    if not playAgain():
        break





    
