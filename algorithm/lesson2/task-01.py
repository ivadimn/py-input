# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


print("Ноль в качестве знака операции завершит работу программы")
while True:
    z = input("Введите знак операции (+,-,*,/) или 0 для завершения: ")
    if z == '0': break
    x = get_number("Введите число x : ")
    y = get_number("Введите число y : ")
    if z in ('+','-','*','/'):
        if z == '+':
            print(f"Резульат x {z} y = {x + y}")
        elif z == '-':
            print(f"Резульат x {z} y = {x - y}")
        elif z == '*':
            print(f"Резульат x {z} y = {x * y}")
        elif z == '/':
            if y != 0:
                print(f"Резульат x {z} y = {x / y}")
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
