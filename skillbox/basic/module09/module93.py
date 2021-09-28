"""
phrase = "Python!"
for symbol in phrase:
    print(symbol)

text = input("Введите текст: ")
for symbol in text:
    print(symbol * 3)
"""

text = input("Введите текст: ")
upper_case_count = 0
lower_case_count = 0
for symbol in text:
    if symbol == "ы":
        lower_case_count += 1
    if symbol == "Ы":
        upper_case_count += 1
print("Больших букв Ы:", upper_case_count)
print("Маленьких букв Ы:", lower_case_count)