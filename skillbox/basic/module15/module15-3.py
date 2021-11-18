"""
words = input("Введите строку: ")
list_char = list(words)
count_replace = 0
for i in range(len(list_char)):
    if list_char[i] == ":":
        list_char[i] = ";"
        count_replace += 1
print("\nИсправленная строка: ", end="")
for ch in list_char:
    print(ch, end = "")
print("\n\nКоличество замен:", count_replace)


string = input("Введите строку: ")
list_char = list(string)
num_char = int(input("Номер символа: "))
index = num_char - 1
if index - 1 >= 0:
    print("\nСимвол слева:", list_char[index - 1])
if index + 1 < len(list_char):
    print("\nСимвол справа:", list_char[index + 1])

count_char = list_char.count(list_char[index]) - 1
if count_char > 0:
    print("Есть", count_char, "такой же символ")
else:
    print("Таких же символов нет.")
"""

words = []
count = [0, 0, 0]
for i in range(3):
    print("Введите", i + 1, "слово: ", end = "")
    words.append(input())
word = input("Слово из текста: ")
while word != "end":
    for index in range(len(words)):
        if word == words[index]:
            count[index] += 1
    word = input("Слово из текста: ")
print("\nПодсчёт слов в тексте")
for index in range(len(words)):
    print(words[index], ":", count[index])
