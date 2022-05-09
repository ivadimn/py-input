import random
vv = ["R", "S", "P"]
wins = ["RS", "SP", "PR"]

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





