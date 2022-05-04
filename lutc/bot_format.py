from random import randint

from telebot import TeleBot, types
from telebot.types import Message

bot = TeleBot("5169533486:AAGr38VTKICdeAPZHQpiiqT26gT3rzZdF1Q")

ll = [
    "<b>bold</b>",
    "<strong>bold</strong>",
    "<i>italic</i>",
    "<em>italic</em>",
    "<a href='URL'>inline URL</a>",
    "<code>inline fixed-width code</code>",
    "<pre>pre-formatted fixed-width code block</pre>"
]


@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button_1 = types.KeyboardButton(text="С пюрешкой")
    # keyboard.add(button_1)
    # button_2 = "Без пюрешки"
    # keyboard.add(button_2)
    # buttons = ["С пюрешкой", "Без пюрешки"]
    # keyboard.add(*buttons)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
                                      request_poll=types.KeyboardButtonPollType()))
    bot.send_message(m.chat.id, "Как подавать котлеты?", reply_markup=keyboard)

    """
    bot.send_message(m.chat.id, "*жирный*", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "~зачеркнутый~", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "_курсив_", parse_mode="MarkdownV2")
    bot.send_message(m.chat.id, "__подчёркнутый__", parse_mode="MarkdownV2")
    for l in ll:
        bot.send_message(m.chat.id, l, parse_mode='HTML', disable_web_page_preview=True)
    """


@bot.message_handler(commands=['inline_url'])
def handle_url(m: Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    bot.send_message(m.chat.id, "Кнопки ссылки", reply_markup=keyboard)


@bot.message_handler(commands=["random"])
def cmd_random(m: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    bot.send_message(m.chat.id, "Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@bot.callback_query_handler(text="random_value", func = lambda call: True)
async def send_random_value(call: types.CallbackQuery):
    print("сработало")
    bot.send_message(call.message.chat.id, str(randint(1, 10)))


@bot.message_handler(content_types=['text', 'contact'])
def handle(m: Message):
    contact = m
    print(contact.json.get("contact"))


bot.polling()
