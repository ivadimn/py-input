# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


number = get_number("Введите натуральное число : ")
even = 0
odd = 0
while number > 0:
    if (number % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10

print(f"Количество чётных чисел = {even}")
print(f"Количество нечётных чисел = {odd}")