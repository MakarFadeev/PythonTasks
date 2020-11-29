import telebot
import datetime

bot = telebot.TeleBot('1415519306:AAErJu_T3Rqti8rIvFglWCyLxBIPX1mS3qc')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет', 'Пока', 'Дата', 'Время', 'День недели')
@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, человек', reply_markup = keybord1)
@bot.message_handler(content_types = ['text'])
def send_text(message):
    if (message.text.upper() == 'ПРИВЕТ'):
        bot.send_message(message.chat.id, 'Привет!')
    elif (message.text.upper() == 'ПОКА'):
        bot.send_message(message.chat.id, 'Пока!')
    elif (message.text.upper() == 'ДАТА'):
        forTest = datetime.datetime.today()
        bot.send_message(message.chat.id, str(forTest.day) + '.' + str(forTest.month) + '.' + str(forTest.year))
    elif (message.text.upper() == 'ВРЕМЯ'):
        forTest = datetime.datetime.now()
        bot.send_message(message.chat.id, str(forTest.hour) + ':' + str(forTest.minute) + ':' + str(forTest.second))
    elif (message.text.upper() == 'ДЕНЬ НЕДЕЛИ'):
        forTest = datetime.datetime.today()
        bot.send_message(message.chat.id, str(forTest.strftime('%A')))

bot.polling()

