import sys

def whos_first(p1, p2):
    if len(p1) > len(p2):
        return "p1"
    elif len(p2) > len(p1):
        return "p2"
    else:
        "tie"

def calc_dice(lst):
    s = 0
    for one, two in lst:
        if one == two:
            return 0
        else:
            s += (one + two)
    return s

def take_wands(wands_count: int, player : str) -> int:
    print(f"Осталось {wands_count} палочел.")
    wands = int(input("{0} сколько палочен возмёте (не больше 3)? ".format(player)))
    return wands

wands_count = int(input("Введите количество палочек для игры: "))
name1 = input("Введите имя первого игрока: ")
name2 = input("Введите имя второго игрока: ")
names = [name1, name2]
name_index = 0
while wands_count > 0:
    wc = take_wands(wands_count, names[name_index])
    name_index = len(names) - name_index - 1
    wands_count -= wc
print("Выиграл: {0}".format(names[name_index]))
