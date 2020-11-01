iSay = input('Введите фразу: ')
print('Введите 2 слова из этой фразы')
iFind1 = input('Первое: ')
iFind2 = input('Второе: ')
word1 = iSay.find(iFind1)
word2 = iSay.find(iFind2)
if (word1 < word2):
    print('ДА')
else:
    print('НЕТ')
