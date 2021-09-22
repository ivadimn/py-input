total_hours = int(input("Введите общее количество часов: "))
cell = 1
for hour in range(1, total_hours // 3 + 1):
    cell *= 2
    print("Прошло:", hour * 3, "часов")
    print("Клеток:", cell)
    print("Часов до конца эксперимента:", total_hours - hour * 3)
    print("-" * 20)
print("Конец эксперимента!")

