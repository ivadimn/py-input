"""
def summa_n(number):
    summ = 0
    for n in range(1, number + 1):
        summ += n
    return summ

number = int(input("Введите число: "))
summ = summa_n(number)
print(summ)
print(summa_n(summ))


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("НОД = ", gcd(a, b))
"""

def numeral_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

count_numbers = int(input("Введите количество задач: "))
max_count = 0
index = 0
for n in range(1, count_numbers + 1):
    number = int(input("Введите задачу: "))
    count = numeral_count(number)
    if count > max_count:
        max_count = count
        index = n
print("Первая задача на обработку с номером:", index)
