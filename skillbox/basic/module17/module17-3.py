"""
first_num = int(input("Первое число: "))
second_num = int(input("Второе число: "))

list_evens = [n for n in range(first_num, second_num + 1) if n % 2 == 0]
print(list_evens)


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = [price if price > 0 else 0 for price in original_prices]
print(new_prices)
"""
import random

list_monstrs1 = [random.randint(50, 80) for _ in range(10)]
list_monstrs2 = [random.randint(30, 60) for _ in range(10)]

list_states = ["Погиб" if list_monstrs1[i] + list_monstrs2[i] > 100 else "Выжил" for i in range(10)]

print("Урон первого отряда: ", list_monstrs1)
print("Урон второго отряда: ", list_monstrs2)
print("Состояние третьего отряда: ", list_states)