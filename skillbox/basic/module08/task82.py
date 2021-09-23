"""
numbers = int(input("Введите количество чисел "))
for number in range(1, numbers // 2 + 1):
    n = number * 2
    print("Число", n, " ** 3 равно", n ** 3)

total_hours = int(input("Введите общее количество часов: "))
cell = 1
for hour in range(1, total_hours // 3 + 1):
    cell *= 2
    print("Прошло:", hour * 3, "часов")
    print("Клеток:", cell)
    print("Часов до конца эксперимента:", total_hours - hour * 3)
    print("-" * 20)
print("Конец эксперимента!")
"""

numbers = int(input("Введите количество чисел "))
for number in range(numbers // 2):
    n = number * 2 + 1
    print("Число", n, " ** 3 равно", n ** 3)

