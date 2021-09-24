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
if begin // delimiter > 1:
    begin += begin % delimiter
elif begin // delimiter == 1 and begin % delimiter != 0:
    begin = delimiter * 2

for number in range(begin, end + 1, delimiter):
    summ += number
    count_numbers += 1
print("Среднее арифметическое чисел кратных", delimiter, "равно", summ / count_numbers)


begin = int(input("Введите начало отрезка: "))
end = int(input("Введидте конец отрезка: "))
step = int(input("Введите шаг: "))
if step > 0:
    step = -step
for number in range(end, begin - 1, step):
    y = number ** 3 + 2 * (number ** 2) - 4 * number + 1
    print("Значение функции y = x^3 + 2x^2 -4x + 1 в точке", number, "равно", y)
"""
envelope_length = 12
envelope_width = 12
letter_length = int(input("Введите длину "))
letter_width = int(input())




