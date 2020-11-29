import random
verb = [' летел.', ' бегал.', ' прыгал.', ' рисовал.', ' считал.', ' говорил.', ' молчал.', ' спорил.', ' танцевал.']
whichVerb = random.randint(0, len(verb) - 1)
noun = ['Вася ', 'Иностранец ', 'Он ', 'Инопланетянин ', 'Человек ', 'Учитель русского языка ']
whichNoun = random.randint(0, len(noun) - 1)
adjective = [' красиво ', ' грубо ', ' легко ', ' странно ', ' не ', ' серьёзно ']
whichAdjective = random.randint(0, len(adjective) - 1)
print(noun[whichNoun], adjective[whichAdjective], verb[whichVerb])
