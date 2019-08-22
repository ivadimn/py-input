import random


def game_number():
    print('Загадай число от 1 до 100 и я его отгадаю за 7 попыток!')

    min_n = 1
    max_n = 100

    ans = None

    while ans != '=':
        current = (min_n + max_n) // 2
        ans = input('Ваше число {} ?: '.format(current))
        if ans == '<':
            min_n = current + 1
        else:
            max_n = current - 1

    print('Конец')


def game():
    print('Я загадал число от 1 до 100. Попробуй его отгадать!')
    i = random.randint(1, 100)
    step = 0

    while True:
        step += 1
        number = int(input(f'Попытка {step}. Ваше число: '))
        if number > i:
            print('Ваше число больше загаданного')
        elif number < i:
            print('Ваше число меньше загаданного')
        else:
            print(f'Угадали с {step} попытки!')
            break

    print('Конец игры!')
