# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = int(input("Введите номер буквы в алфавите : "))
a = ord("a")
max_number = ord("z") - a + 1
if number > max_number:
    print("Такой буквы нет")
else:
    char = chr(a + number - 1)
    print(f"Буква с номером {number} - {char}")