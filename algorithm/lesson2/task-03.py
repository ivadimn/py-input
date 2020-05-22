# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


number = get_number("Введите натуральное число : ")
print(f"Введённое число = {number}")
exp = len(str(number)) - 1
reversed_number = 0
while number > 0:
    reversed_number += (number % 10) * (10 ** exp)
    number //= 10
    exp -= 1
print(f"Обратное число = {reversed_number}")