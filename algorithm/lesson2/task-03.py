# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


str_num = str(get_number("Введите натуральное число : "))
print(f"Введённое число = {str_num}")
str_num = list(str_num)
len_str = len(str_num)
for i in range(0, len_str // 2):
    temp = str_num[i]
    str_num[i] = str_num[len_str - i - 1]
    str_num[len_str - i - 1] = temp
print(f"Обратное число = {''.join(str_num)}")