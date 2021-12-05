"""
words = input("Введите три слова серез пробел: ").split()
text = input("Введите текст: ").split()
for word in words:
    print("Слово", word, "встречается в тексте", text.count(word), "раз")


text = input("Введите текст: ").split()
print("Исправленный текст:", " ".join(text))
"""

template = input("Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ")
mans = input("Список людей через запятую: ").split(", ")
ages = list(map(int, input("Возраст людей через пробел: ").split()))

for i_man in range(len(mans)):
    print(template.format(name = mans[i_man], age = ages[i_man]))

people = [" ".join([mans[i], str(ages[i])]) for i in range(len(mans))]
people_str = ", ".join(people)
print("\nИменинники:", people_str)

