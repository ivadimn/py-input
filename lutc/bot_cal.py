from telebot import TeleBot

from telegram_bot_calendar import WMonthTelegramCalendar, DetailedTelegramCalendar, LSTEP

bot = TeleBot("5169533486:AAGr38VTKICdeAPZHQpiiqT26gT3rzZdF1Q")


@bot.message_handler(commands=['start'])
def start(m):

    #calendar, step = DetailedTelegramCalendar().build()
    mc = WMonthTelegramCalendar()
    mc.locale = "ru"
    calendar, step = mc.build()

    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    print(c.data)
    result, key, step = DetailedTelegramCalendar().process(c.data)
    print(result)
    print(key)
    print(step)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)


bot.polling()