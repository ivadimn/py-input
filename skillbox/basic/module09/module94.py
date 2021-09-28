"""
print("-" * 10)
for step in range(4):
    print("|", end="")
    print("0" * 8, end="")
    print("|")
print("-" * 10)


first = int(input("Введите первую четверть IP адреса: "))
step = int(input("Введите величину шага: "))
summ = first
print("IP адрес:", first, end=".")
for i in range(2):
    first += step
    print(first, end=".")
    summ +=  first
print(summ)
"""

number = int(input("Введите число: "))
print("-=-", end="")
for n in range(0, number + 1, 10):
    print(n, end="-=-")