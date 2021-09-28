"""
day_of_week = input("Введите день недели: ")
day_number = 0
for day in "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье":
    day_number += 1
    if day == day_of_week:
        print("Номер дня недели: ", day_number)
        break


caramba_count = 0
for _ in range(10):
    word = input("Введите слово: ")
    if word == "Карамба":
        caramba_count += 1
print("На корабль попадут", caramba_count, "чел.")


text = input("Введите текст: ")
position = 0
for symbol in text:
    position += 1
    if symbol == "*":
        print("Символ ‘*’ стоит на позиции", position)
        break


rows = int(input("Введите кол-во рядов: "))
seats = int(input("Введите кол-во сижений: "))
meters = int(input("Введите кол-во метров между рядами: "))
print("Сцена\n")
for _ in range(rows):
    print("=" * seats, end = " ")
    print("*" * meters, end = " ")
    print("=" * seats)
"""




