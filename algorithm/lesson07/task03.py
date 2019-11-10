# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

size = 10
array = [random.randint(0, 50) for i in range(2 * 10 + 1)]
print(array)



def select(a, k):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param a: список числовых данных
    :param k: индекс
    :return: k-тый элемент l
    """
    if len(a) == 1:
        return a[0]

    point = random.choice(a)

    lows = [e for e in a if e < point]
    highs = [e for e in a if e > point]
    points = [e for e in a if e == point]

    if k < len(lows):
        return select(lows, k)
    elif k < len(lows) + len(points):
        # угадали медиану
        return points[0]
    else:
        return select(highs, k - len(lows) - len(points))


def median(a):
    if len(a) % 2 == 1:
        return select(a, len(a) / 2)
    else:
        return 0.5 * (select(a, len(a) / 2 - 1) + select(a, len(a) / 2))

m = median(array)
print(f"Медиана = {m}")
print("Для проверки : ")
print(sorted(array))
print(m)