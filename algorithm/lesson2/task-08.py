# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


count_num = get_number("Введите количество чисел для поиска: ")
digit = get_number("Введите цифру которую будем искать в числах: ")
count_total = 0
for i in range(count_num):
    number = get_number(f"Введите {i + 1} число : ")
    count_in = 0
    n = number
    while n > 0:
        if n % 10 == digit:
            count_in += 1
        n //= 10
    print(f"В числе {number} цифра {digit} встречается {count_in} раз ")
    count_total += count_in
print(f"Цифра {digit} во всех числах встретилась {count_total} раз! ")
