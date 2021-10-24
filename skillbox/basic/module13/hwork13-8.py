import math

x = float(input("Введите действительное число x: "))
precision = float(input("Введите точность вычиления: "))
summ = 1
n = 1
member = 1
while abs(member) > precision:
    member = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    summ += member
    n += 1
print("Сумма ряда:", summ)