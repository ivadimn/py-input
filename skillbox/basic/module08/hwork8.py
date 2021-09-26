"""
total_buckwheat = 100
month_limit = 4
months = 0
for buckwheat in range(total_buckwheat, -1, -month_limit):
    print("Через", months, "месяцев гречки должно быть", buckwheat, "кг." )
    months += 1

debtors = int(input("Сколько должников у банка? "))
debt = 0
for debtor in range(0, debtors + 1, 5):
    print("Должник с номером", debtor)
    debt += int(input("Сколько должны? "))
print("Общая сумма долга:", debt)

seconds = int(input("Через сколько секунд должна взорваться бомба? "))
for second in range(seconds, 0, -1):
    print("До взрыва осталось", second, "сек.")
    answer = input("Хотите ли вы обезвредить бомбу сейчас? ")
    if answer == "да":
        break
if second == 1 and answer != "да":
    print("Бомба взорвалась")
else:
    print("Бомба обезврежена, до взрыва оставалось", second, "сек.")

begin = int(input("Введите начало отрезка: "))
end = int(input("Введидте конец отрезка: "))
delimiter = int(input("Введите число, которому должны быть кратны числа в отрезке: "))
summ = 0
count_numbers = 0
relation = begin // delimiter
if  1 < relation < 2:
    begin += begin % delimiter
elif begin // delimiter == 0:
    begin = delimiter
else:
    if begin % delimiter != 0:
        begin = begin - (begin % delimiter) + delimiter


for number in range(begin, end + 1, delimiter):
    summ += number
    count_numbers += 1
    print(number)
if count_numbers == 0:
    print("Чисел кратных", delimiter, "в отрезке [", begin, ",", end, "] нет")
else:
    print("Среднее арифметическое чисел кратных", delimiter, "равно", summ / count_numbers)


begin = int(input("Введите начало отрезка: "))
end = int(input("Введидте конец отрезка: "))
step = int(input("Введите шаг: "))
if step > 0:
    step = -step
for number in range(end, begin - 1, step):
    y = number ** 3 + 2 * (number ** 2) - 4 * number + 1
    print("Значение функции y = x^3 + 2x^2 -4x + 1 в точке", number, "равно", y)


envelope_length = 12
letter_length = int(input("Введите длину листа бумаги: "))
half_count = 0
while letter_length > envelope_length:
    half_count += 2
    letter_length /= 2
print("Письмо нужно сложить", half_count, "раз чтобы оно поместилось в конверт!")


educational_grant = int(input("Введите размер стипендии: "))
expenses = int(input("Введите начальную сумму расходов на проживание: "))
total_expenses = 0
for month in range(10):
    total_expenses += expenses
    expenses += expenses * 0.03
print("У родителей необходимо получить: ", int(total_expenses + 1) - educational_grant * 10, "руб.")


number = int(input("Введите натуральное число: "))
summ = 1
for n in range(1, number + 1):
    summ += 1 / (2 ** n) * (-1) ** n
print("СУмма ряла равна: ", summ)


x = int(input("Введите число x: "))
mult_up = 1
mult_down = 1
for p in range(1, 7):
    mult_up *= (x - (2 ** p - 1))
    mult_down *= (x - 2 ** p)
if mult_down != 0:
    print("Значение выражения равно:", mult_up / mult_down)
else:
    print("Значение выражения в знаменателе равно 0")
"""

boys = int(input("Введите кол-во мальчиков: "))
girls = int(input("Введите кол-во девочек: "))
bigger, smaller = boys, girls
b_char, s_char = "B", "G"
bound = 1
if boys < girls:
    bigger, smaller = girls, boys
    b_char, s_char = "G", "B"
s = ""
if bigger > (smaller * 2):
    s = "Решения нет"
else:
    bound = bigger - smaller
    for bgb in range(bound):
        s += b_char + s_char + b_char
    for bg in range(smaller - bound):
        s += b_char + s_char
print("Ответ:", s)
