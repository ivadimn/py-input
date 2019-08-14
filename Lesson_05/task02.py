# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random

items = [1, 2, 3, 4, 23, 89, 34, "123", "789", 257]
empty_items = []


def get_random_item(list):
    return random.choice(list) if len(list) > 0 else None


if __name__ == '__main__':
    print("Случайно выбранный элемент - ", get_random_item(items))
    print("Случайно выбранный элемент - ", get_random_item(empty_items))