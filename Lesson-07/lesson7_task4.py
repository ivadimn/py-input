'''
4. Написать функцию которая принимает на вход число от 1 до 100.
Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
возведенное в квадрат.
Далее написать основной код программы.
Пользователь вводит число.
Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
'''


def my_f(i):
    if i == 13:
        raise Exception("число = 13")
    else:
        i = i**2
        return i


i = int(input('Введите число: '))

try:
    res = my_f(i)
except Exception:
    print('Ошибка, введено число 13!')
else:
    print(res)