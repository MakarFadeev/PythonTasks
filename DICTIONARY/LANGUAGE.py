from DICTIONARY import slovar
eng_words = None
rus_words = None

def eng(word):
    eng_words = dict([[v, k] for k, v in slovar.items()])
    return eng_words[word]

def rus(word):
    rus_words = dict([[k, v] for v, k in slovar.items()])
    return rus_words[word]

while True:
    find_word = input('Введите слово: ')
    print(rus(find_word))
    print(find_word)
    
