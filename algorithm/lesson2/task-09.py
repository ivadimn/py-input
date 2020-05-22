# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def get_number(s: str) -> int:
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Вы ввели не целое число!")
            continue


count_num = get_number("Введите количество чисел для анализа: ")
max_number = 0
max_summa = 0
for i in range(count_num):
    number = get_number(f"Введите {i + 1} число : ")
    summa = 0
    n = number
    while n > 0:
        summa += n % 10
        n //= 10
    if summa > max_summa:
        max_summa = summa
        max_number = number
print(f"Наибольшее по сумме цифр число - {max_number} сумма его цифр {max_summa}! ")