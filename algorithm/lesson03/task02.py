# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5, если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
from random import randint
first = [randint(1, 99) for _ in range(50)]
indexes = []
for i, item in enumerate(first):
    if item % 2 == 0:
        indexes.append(i)

print(first)
print("Индексы чётных элементов массива :")
print(indexes)
