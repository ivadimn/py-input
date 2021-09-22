""" 1 number = int(input("Введите конечное число: "))
number_count = 1
while number_count <= number:
    print(number_count ** 3)
    number_count += 1"""

"""2 name = input("Имя должника? ")
summa = int(input("Сумма долга? "))
while summa > 0:
    repay = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    summa -= repay
    if summa > 0:
        print("Маловато,", name + ".",  "Давайте ещё раз")
print("Отлично,", name + "!", "Вы погасили долг. Спасибо!")"""

"""3 number = int(input("Введите число: "))
count_digit = 0
while number > 0:
    number //= 10
    count_digit += 1
print("Количество десятичных знаков: ", count_digit)"""


""" 4 count_even = 0
while True:
    number = int(input("Введите очередное число последовательности или 0 для завершения: "))
    if number == 0:
        break
    elif number % 2 > 0:
        continue
    else:
        count_even += 1
print("Количество чётных чисел в последовательности: ", count_even)"""


"""5 ticket_number = int(input("Введите номер билета (6 цифр): "))
first_summa = 0
second_summa = 0
while ticket_number > 0:
    digit = ticket_number % 10
    if ticket_number > 1000:
        first_summa += digit
    else:
        second_summa += digit
    ticket_number //= 10

if first_summa == second_summa:
    print("Вам повезло билет счастливый!!!")
else:
    print("К сожалению билет не счастливый")"""

"""count_positive = 0
count_negative = 0
while True:
    number = int(input("Введите число (или 0 для завершения): "))
    if number == 0:
        break
    elif number > 0:
        count_positive += 1
    else:
        count_negative += 1
print("Количество положительных чисел:", count_positive)
print("Количество отрицательных чисел:", count_negative)"""

"""count_hours = 1
count_task = 0
is_shoping = False
print("Начался 8-часовой рабочий день")
while count_hours <= 8:
    print(count_hours, "-й час")
    count_task += int(input("Сколько задач решит Максим? "))
    is_answer = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if is_answer > 0:
        is_shoping = True
    count_hours += 1
print("Рабочий день закончился. Всего выполнено задач:", count_task)
if is_shoping:
    print("Нужно зайти в магазин.")"""

"""current_summa = int(input("Сколько сейчас денег в банке? "))
percent = int(input("Укажите процентную ставку? "))
target_summa = int(input("Какую сумму вы хотите получить? "))
years = 0
while current_summa < target_summa:
    current_summa += int(current_summa / 100 * percent)
    years += 1
print("вы получите нужную сумму через", years, "лет")"""


"""target_number = 7
count_step = 0
while True:
    number = int(input("Введите число: "))
    count_step += 1
    if number > target_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif number < target_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", count_step)
        break
"""

target_number = int(input("Загадайте число между 1 и 100 (включительно): "))
low = 1
high = 100
count_step = 0
while True:
    number = (low + high) // 2
    print("Твоё число равно(1), больше(2) или меньше(3), чем число", number, "?")
    result = int(input())
    count_step += 1
    if result == 1:
        print("Я угадал число:", number, "c", count_step, "попыток")
        break
    elif result == 2:
        low = number + 1
    elif result == 3:
        high = number - 1
    else:
        print("Введено неверное значение, будте анимательней!!!")




