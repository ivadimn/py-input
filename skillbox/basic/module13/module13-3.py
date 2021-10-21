"""
n = 1
count = 0
while n != 0:
    n /= 2
    count += 1
    print(n)
print(count)

x = 1
count = 0
n = float(input("Введите число в экспоненциальной форме: "))
while x <= 2:
    x += n
    count += 1
print(x)
print(count)
"""

x = float(input("Введите число больше 10: "))
rang = 0
while x >= 10:
    x /= 10
    rang += 1
print("x =", x, "* 10 **", rang)