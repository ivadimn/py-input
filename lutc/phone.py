import random
vv = ["R", "S", "P"]
wins = ["RS", "SP", "PR"]


class Item:
    def __init__(self, name: str, distance: float) -> None:
        self.name = name
        self.distance = distance

    def __repr__(self):
        return "Item: {0} - {1}".format(self.name, self.distance)



"""
while True:
    vu = input("Введите ваш вариант (R - камень, S - ножницы, P - бумага): ").upper()
    v = random.choice(vv)
    print(f"Ваш выбор: {vu} Выбор компьютера: {v}")
    if vu == v:
        print("Ничья")
    elif f"{vu}{v}" in wins:
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")
    if input("Хотите продолжить? ").lower() != "да":
        break
"""

f = lambda item: 2 <= item.distance <= 8

items = [Item("111aaa", 10.2), Item("aaa11", 0.2), Item("2222", 5.1), Item("3333", 8.3),
        Item("4444", 1.2), Item("5555", 2.5), Item("6666", 11.2), Item("77777", 3.4)]

items_sel = filter(f, items)
print(list(items_sel))





