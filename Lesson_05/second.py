# 2: Создайте модуль. В нем создайте функцию,
# которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None.
# Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную.
#     Или возьмите этот: [1, 2, 3, 4]

import random
l = [1, 2, 3, 4]
if __name__ == "__main__":
    print(type(l))

def element(n):
    if len(n) == 0:
        print("None")
    else:
        e = random.choice(n)
        print(e)

element(l)