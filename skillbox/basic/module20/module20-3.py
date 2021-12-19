import random
"""
line = input("Строка: ")
for i, ch in enumerate(line):
    if ch == "~":
        print(i)


def create_dict(l : list):
    d = dict()
    for i, ch in enumerate(l):
        d[i] = ch
    return d

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
list1 = [random.choice(alphabet) for _ in range(10)]
list2 = [random.choice(alphabet) for _ in range(10)]
print("Первый список: ", list1)
print("Второй список: ", list2)

print("Первый словарь: ", create_dict(list1))
print("Второй словарь: ", create_dict(list2))
"""

def create_list(iter_obj):
    if isinstance(iter_obj, dict):
        return [{k: iter_obj[k]} for i, k in enumerate(iter_obj) if i % 2 == 0]
    elif isinstance(iter_obj, str) or isinstance(iter_obj, list) or isinstance(iter_obj, tuple):
        return [v for i, v in enumerate(iter_obj) if i % 2 == 0]
    else:
        return []

d = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}
print(create_list(d))