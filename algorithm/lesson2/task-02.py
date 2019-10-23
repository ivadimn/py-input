# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


str_num = str(get_number("Введите натуральное число : "))
even = []
odd = []
for i in range(0, len(str_num)):
    if int(str_num[i]) % 2 == 0:
        even.append(int(str_num[i]))
    else:
        odd.append(int(str_num[i]))

print(f"Количество чётных чисел = {len(even)} : {even}")
print(f"Количество нечётных чисел = {len(odd)} : {odd}")