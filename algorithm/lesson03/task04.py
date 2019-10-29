# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint


def max_keys(d :dict) -> list:
    max_item = 0
    maxs = []
    for key in d.keys():
        if d[key] > max_item:
            max_item = d[key]
            result_key = key
    maxs.append(result_key)
    for key in d.keys():
        if d[key] == max_item and key != result_key:
            maxs.append(key)
    return maxs


array = [randint(1, 20) for _ in range(100)]
print("Исходный массив : ")
print(array)
frequency = {}
for item in array:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Частоты")
print(frequency)
print("Самые часто встречающиеся элементы : ")
print(max_keys(frequency))

