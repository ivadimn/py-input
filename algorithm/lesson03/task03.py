# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


array = [randint(1, 99) for _ in range(50)]
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

print(f"Максимальный элемент = {array[index_max]}")
print(f"Минимальный элемент = {array[index_min]}")
spam = array[index_max]
array[index_max] = array[index_min]
array[index_min] = spam
print("Массив после перестановки элементов : ")
print(array)