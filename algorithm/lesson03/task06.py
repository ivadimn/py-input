# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint


array = [randint(1, 20) for _ in range(50)]
print("Исходный массив : ")
print(array)
max_item = array[0]
index_max = 0
min_item = array[0]
index_min = 0
for i, item in enumerate(array):
    if item > max_item:
        max_item = item
        index_max = i
    if item < min_item:
        min_item = item
        index_min = i


print(f"Максимальный элемент с индексом {index_max} = {array[index_max]}")
print(f"Минимальный элемент с индексом {index_min} = {array[index_min]}")
if index_min < index_max:
    start = index_min + 1
    finish = index_max
elif index_min > index_max:
    start = index_max + 1
    finish = index_min
summa = 0
for n in array[start:finish]:
    summa += n
print(f"Сумма элементов между максимальным и минимальным = {summa}")

