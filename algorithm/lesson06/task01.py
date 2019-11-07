# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Используется задача вычисления  сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# # Количество элементов (n) передаётся параметром.

# 1 Вариант: - сложение членов последовательности
import sys
from funcs import show_sizeof

print(sys.platform)
print(sys.version)

q = -0.5
summa = 0
show_sizeof(q)
show_sizeof(summa)
for i in range(0, 1000):
    summa += q ** i
show_sizeof(summa)
show_sizeof(range(0, 1000))
print(sys.getsizeof(range(0, 1000)))
show_sizeof(summa)