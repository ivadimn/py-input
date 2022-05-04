from telebot import TeleBot, types
from telebot.types import Message

bot = TeleBot("5169533486:AAGr38VTKICdeAPZHQpiiqT26gT3rzZdF1Q")


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Выбери меня')
    msg = bot.send_message(message.chat.id, text = 'Нажми кнопку в меню', reply_markup = keyboard )


@bot.message_handler(content_types = ['text'])
def step1(message):
    menu1 = types.InlineKeyboardMarkup()
    menu1.add(types.InlineKeyboardButton(text = 'Первая кнопка', callback_data ='first'))
    menu1.add(types.InlineKeyboardButton(text = 'Вторая кнопка', callback_data ='second'))

    if message.text == 'Выбери меня':
        msg = bot.send_message(message.chat.id, text ='Нажми первую inline кнопку', reply_markup = menu1)

@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2 = types.InlineKeyboardMarkup()
    menu2.add(types.InlineKeyboardButton(text = 'Третья кнопка', callback_data ='third'))
    menu2.add(types.InlineKeyboardButton(text = 'Четвертая кнопка', callback_data ='fourth'))

    if call.data == 'first':
        msg = bot.send_message(call.message.chat.id, 'Нажми третью кнопку', reply_markup = menu2)
    elif call.data == 'third':
        msg = bot.send_message(call.message.chat.id, 'Конец')
        

bot.polling()