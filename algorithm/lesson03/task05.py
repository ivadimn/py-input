# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import sys
from random import randint


array = [randint(-50, 50) for _ in range(50)]
print("Исходный массив : ")
print(array)
max_negative = -sys.maxsize - 1
for n in array:
    if n < 0 and n > max_negative:
        max_negative = n
print(f"Максимальный отрицательный элемент - {max_negative}")
