import datetime
import time
import random
messages = [
"Из всех деревьев мы врезались в то, которое смогло дать нам сдачи.",
"Если не прекратить его попытки спасти вам жизнь, он вас убьет.",
"Нашу сущность намного лучше демонстрируют действия, а не возможности.",
"Я маг, а не размахивающий палкой бабуин.",
"Величие порождает зависть, зависть - злобу, злоба - ложь.",
"В мечтах мы попадаем в наш и только наш мир.",
"Я убежден, что истина, как правило, предпочтительнее лжи.",
"Казалось, что рассвет следует за полночью с неприличной поспешностью." 
]
print('Проверка скорости набора. Введите следующую фразу. Я засеку время…')
time.sleep(2)
print('Приготовиться…')
time.sleep(1)
print('Сосредоточиться…')
time.sleep(1)
print('Начали:')
random_number = random.randint(0, 7)
print(messages[random_number])
start_time = datetime.datetime.now()
answer = input()
end_time = datetime.datetime.now()
delta = end_time - start_time
delta = delta.seconds + delta.microseconds / 1000000
speed = int(len(messages[random_number])) / int(delta)
print('Отлично! вы вывели целых ', len(messages[random_number]), ' символов за ', delta, ' секунд!')
print('Также я определил, что ваша скорость печатания - ', speed, ' символов в секунду!')
if (answer == messages[random_number]):
    print('Также у вас получилось написать текст без ошибок! Поздравляю!')
else:
    print('К сожалению, вы допустили как минимум 1 ошибку!')
