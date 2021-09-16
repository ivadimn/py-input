"""
for number in 114,12,14,10605,4907,450:
    if number % 2 == 0 and number % 3 == 0:
        print(number, 'Подходит')
    else:
        print(number, 'Не подходит')

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))
n3 = int(input("Введите третье число: "))
n4 = int(input("Введите четвёртое число: "))
n5 = int(input("Введите пятое число: "))
n6 = int(input("Введите шестое число: "))
n7 = int(input("Введите седьмое число: "))
n8 = int(input("Введите восьмое число: "))
n9 = int(input("Введите девято число: "))
n10 = int(input("Введите десятое число: "))
right_numbers = 0
for n in n1,n2,n3,n4,n5,n6,n7,n8,n9,n10:
    if n > 0 and n % 2 == 0:
        right_numbers += 1
print("Одновременно чётных и положительных чисел: ", right_numbers)

s1 = int(input("Введите зарплату за 1 месяц: "))
s2 = int(input("Введите зарплату за 2 месяц: "))
s3 = int(input("Введите зарплату за 3 месяц: "))
s4 = int(input("Введите зарплату за 4 месяц: "))
s5 = int(input("Введите зарплату за 5 месяц: "))
s6 = int(input("Введите зарплату за 6 месяц: "))
s7 = int(input("Введите зарплату за 7 месяц: "))
s8 = int(input("Введите зарплату за 8 месяц: "))
s9 = int(input("Введите зарплату за 9 месяц: "))
s10 = int(input("Введите зарплату за 10 месяц:: "))
s11 = int(input("Введите зарплату за 11 месяц:: "))
s12 = int(input("Введите зарплату за 12 месяц:: "))
year_salary = 0
for s in s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12:
    year_salary += s
print("Средняя зарплата за 12 месяцев составила: ", year_salary / 12)

contrs = 0
for sector in range(30, 36):
    print("Людей в", sector, "секторе: ", end="")
    people = int(input())
    if people < 10:
        print("Всё спокойно")
    else:
        print("Нарушение! Слишком много людей в секторе!")
        contrs += 1
print("Количество нарушений:", contrs)

number = int(input("Введите число: "))
factorial = 1
for n in range(2, number + 1):
    factorial *= n
print("Факториал числа", number, "равен",  factorial)

pupils = int(input("Сколько учеников в классе? "))
total_excellent = 0
total_good = 0
total_bad = 0
for p in range(1, pupils + 1):
    print("Какую оценку получил", p, "ученик? ", end="")
    ball = int(input())
    if ball == 5:
        total_excellent += 1
    elif ball == 4:
        total_good += 1
    elif ball == 3:
        total_bad += 1

if total_excellent > total_good and total_excellent > total_bad:
    print("сегодня больше всего отличников")
elif total_good > total_excellent and total_good > total_bad:
    print("сегодня больше всего хорошистов")
elif total_bad > total_excellent and total_bad > total_good:
    print("сегодня больше всего троечников")
elif total_excellent == total_good and total_excellent > total_bad:
    print("сегодня больше всего отличников и хорошистов")
elif total_bad == total_good and total_bad > total_excellent:
    print("сегодня больше всего хорошистов и троечников")
elif total_excellent == total_bad and total_excellent > total_good:
    print("сегодня больше всего отличников и троечников")
else:
    print("Сегодня всех поровну")

a = int(input("Введите начало отрезка: "))
b = int(input("Введите конец отрезка: "))
summ = 0
count_right = 0
for n in range(a, b + 1):
    if n % 3 == 0:
        summ += n
        count_right += 1
if count_right > 0:
    print("Cреднее арифметическое всех чисел из отрезка [", a, ";", b, "], которые кратны числу 3: ", summ / count_right)
else:
    print("Чисел кратных 3 нет")

for number in range(10, 100):
    local_number = number
    mult = 1
    while local_number > 0:
        digit = local_number % 10
        mult *= digit
        local_number //= 10
    if (mult * 3) == number:
        print("Замечательное число: ", number)

is_sort = True
prev_number = -1
for n in range(10):
    number = int(input("Введите число: "))
    if number < prev_number:
        is_sort = False
    prev_number = number
if is_sort:
    print("Числа упорядочены по возрастанию")
else:
    print("Числа не упорядочены по возрастанию")"""

summ = 0
count_cards = int(input("Введите количество карточек: "))
for n in range(count_cards - 1):
    print("Введите номер карточки от", 1, "до", count_cards, ": ", end="")
    card_number = int(input())
    summ += card_number
summ_all = 0
for card in range(1, count_cards + 1):
    summ_all += card
print("Номер потерявшейся карточки= =", summ_all - summ)
