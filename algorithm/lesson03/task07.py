#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import sys
from random import randint


array = [randint(1, 20) for _ in range(50)]
print("Исходный массив : ")
print(array)

min_item1 = array[0]
index_min1 = 0
for i, item in enumerate(array):
    if item < min_item1:
        min_item1 = item
        index_min1 = i

array[index_min1] = sys.maxsize
min_item2 = array[0]
index_min2 = 0
for i, item in enumerate(array):
    if item < min_item2:
        min_item2 = item
        index_min2 = i

print(f"Два минимальных элемента массива : ")
print(f"Первый с индексом {index_min1} = {min_item1}")
print(f"Второй с индексом {index_min2} = {min_item2}")