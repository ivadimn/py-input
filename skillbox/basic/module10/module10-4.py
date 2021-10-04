"""
people = int(input("Введите количество людей: "))
for hour in range(people + 1):
    print("После", hour, "часа осталось людей")
    for p in range(hour, people):
        print("Человек №", p, "в очереди")
    print("-" * 20)
print("Очередь обслужена!!")


seqNum = int(input("Введите количество чисел в последовательности: "))
numeralCount = 0
for num in range(seqNum):
    print("Введите", num, "-е число", end = "")
    numeral = int(input())
    while numeral > 0:
        if numeral % 10 > 5:
            numeralCount += 1
        numeral //= 10
print("Количество цифр больше 5:", numeralCount)
"""

size = int(input("Введите размер матрицы: "))
for row in range(size):
    for col in range(row, size):
        print(col, end = " ")
    print()