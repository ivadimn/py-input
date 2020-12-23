import nltk
import random
import json

BOT_CONFIG = {
    "intents" :  { # намерения
        "hello": { # намерение поздороваться
            "examples": ["Привет", "Добрый день", "Шалом", "Здравствуйте"],
            "responses": ["Привет, человек", "Доброго времени суток"],
        },
        "bye": {
            "examples": ["Пока", "Досвидос", "Прощай"],
            "responses": ["Счастливо", "До свидания", "Если что, возвращайтесь"],
        },
        "howdoyoudo": {
            "examples": ["Как дела", "Что делаешь", "Какие дела"],
            "responses": ["Маюсь фигней", "Отвечаю на дурацкие вопросы", "Веду вебинары"],
        },
    },
    "failure_phrases": [
        "Я ничо не понял",
        "Что-то непонятно",
        "Я всего лишь бот, сформулируйте попроще"
    ]
}


def filter(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгджзеёийклмнопрстуфхцчшщьыъэюя -']
    return ''.join(text)


def match(text, example):
    text = filter(text)
    example = filter(example)
    distance = nltk.edit_distance(text, example) / len(example)
    return distance < 0.4


def get_intent(text):
    for intent, data in BOT_CONFIG["intents"].items():
        for example in data["examples"]:
            if match(text, example):
                return intent


def get_answer_by_intent(intent):
    phrases = BOT_CONFIG["intents"][intent]["responses"]
    return random.choice(phrases)


def bot(text):
    intent = get_intent(text)

    if intent:
        return get_answer_by_intent(intent)

    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)


with open("big_bot_config.json", "r") as f:
    BOT_CONFIG = json.load(f)


print(BOT_CONFIG["intents"]["hello"]["examples"])

#question = ""
#while question not in ["выход", "отстань"]:
#    question = input()
#    answer = bot(question)
#    print(answer)

#print(bot("досвидосик"))

