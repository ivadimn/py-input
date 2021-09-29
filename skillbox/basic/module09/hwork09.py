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

length = 20
width = 15
way = " "
pos_x = 10
pos_y = 8
while (way != "x") and (way != "X"):
    print("[Программа]: Марсоход находится на позиции", pos_x,",", pos_y, ",введите команду:")
    way = input("[Оператор (X дя завершения)]: ")
    if (way == "w") or (way == "W"):
        if pos_y > 0:
            pos_y -= 1
    elif (way == "s") or (way == "S"):
        if pos_y < width:
            pos_y += 1
    elif (way == "a") or (way == "A"):
        if pos_x > 0:
            pos_x -= 1
    elif (way == "d") or (way == "D"):
        if pos_x < length:
            pos_x += 1


text = input("Введите строку: ")
max_s = 0
s_count = 0
for symbol in text + "0":
    if symbol == "s":
        s_count += 1
    else:
        if s_count > 0:
            if s_count > max_s:
                max_s = s_count
            s_count = 0
print("Самая длинная последовательность:", max_s)

text = input("Введите текст: ")
max_word = 0
s_count = 0
for symbol in text + " ":
    if symbol == " ":
        if s_count > max_word:
            max_word = s_count
        s_count = 0
    else:
        s_count += 1
print("Длина самого длинного слова:", max_word)


length = int(input("Введите общую длину колонтитула в символах: "))
exclamatory_count = int(input("Введите желаемое количество восклицательных знаков: "))
tilda_count = length - exclamatory_count
print("~" * (tilda_count // 2), end="")
print("!" * exclamatory_count, end="")
if tilda_count % 2 == 0:
    print("~" * (tilda_count // 2))
else:
    print("~" * (tilda_count // 2 + 1))


string = input("Введите строку из 10 символов a и b: ")
milk_volume = 0
for index, symbol in enumerate(string):
    if symbol == "b":
        milk_volume += (index + 1) * 2
print("За день произведено молока:", milk_volume)

"""

encrypt_word = input("Введите зашифрованное сщщбщение: ")
result1 = ""
result2 = ""
index = 1
for symbol in encrypt_word:
    if index % 2 != 0:
        result1 += symbol
    else:
        result2 = symbol + result2
    index += 1
print("Расшифрованное сообщение:", result1 + result2)





