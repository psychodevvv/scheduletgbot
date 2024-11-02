import telebot
from telebot import types
from datetime import datetime

TOKEN = '7794503206:AAEeAlwQgIDUKwZtSHX3YdJy8LgCekqjkcg'

bot = telebot.TeleBot(TOKEN)

schedule_week1 = 'Расписание на эту неделю!\nПонедельник:\nГлобальные компетенции, 713\nМатематика, 303Г\nИнформатика, 611\nВторник:\nКураторский час, 303А\nФизика, 303А\nРусский язык, 503А\nХимия, 411\nНВП, 702\nСреда:\nРусская литература, 706\nФизика, 303А\nФиз-культура, манеж\nЧетверг:\nХимия, 411\nРусская литература, 706\nКазхский язык, 409/304\nМатематика, 303Г\nПятница:\nИстория Казахстана, 716\nАнглийский язык, 704/700\nГеография, 717\nИнформатика, 611'
schedule_week2 = 'Расписание на эту неделю!\nПонедельник:\nФиз-культура, спорт зал\nМатематика, 303Г\nКазахский язык, 409/304\nВторник:\nКураторский час, 305\nАнглийский язык, 704/700\nРусский язык, 503А\nХимия, 411\nНВП, 702\nСреда:\nРусский язык, 503А\nФизика, 303А\nФиз-культура, манеж\nЧетверг:\nХимия, 411\nРусская литература, 706\nКазхский язык, 409/304\nМатематика, 303Г\nПятница:\nИстория Казахстана, 716\nАнглийский язык, 704/700\nГеография, 717\nИнформатика, 611'

def is_even_week():
    current_week = datetime.now().isocalendar()[1]
    if current_week % 2 == 0:
        return schedule_week2
    else:
        return schedule_week1

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.ReplyKeyboardButton('Расписание')
    item2 = types.ReplyKeyboardButton('Связаться')
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Связаться':
            bot.send_message(message.chat.id, 'Староста: https://wa.me/77778246574')
            bot.send_message(message.chat.id, 'Куратор: https://wa.me/77789369902')
        elif message.text == 'Расписание':
            schedule = is_even_week()
            bot.send_message(message.chat.id, schedule)
    
bot.polling(none_stop=True)