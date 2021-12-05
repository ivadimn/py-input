"""
menu = input("Доступное меню: ").split(";")
print("На данный момент в меню есть:", ", ".join(menu))


words = input("Введите слова через пробел: ").split()
max_len_word = words[0]
max_len = len(words[0])
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word
print("Самое длинное слово:", max_len_word, "его длина =", max_len)


spec_ch = tuple("@№$%^&*()")
exts = (".txt", )
file_name = input("Название файла: ")
if file_name.startswith(spec_ch):
    print("Ошибка: название начинается на один из специальных символов")
elif not file_name.endswith((".txt", ".docs")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")


words = input("Введите строку: ").split()
words_cap = [word.capitalize()  for word in words]
print("Результат:", " ".join(words_cap))



def is_pwd_secure(pwd: str):
    is_cap_ch = False
    count_digits = 0
    for ch in pwd:
        if ch.isalpha() and ch.isupper():
            is_cap_ch = True
        elif ch.isdigit():
            count_digits += 1
    return is_cap_ch and count_digits >= 3


password = input("Придумайте пароль: ")
while not is_pwd_secure(password):
    print("Пароль ненадёжный. Попробуйте ещё раз.")
    password = input("Придумайте пароль: ")
print("Это надёжный пароль!")


def encode(text: str):
    index = 0
    encode = []
    while index < len(text):
        ch = text[index]
        count = 1
        index += 1
        while index < len(text) and text[index] == ch:
            count += 1
            index += 1
        encode.append(ch)
        encode.append(str(count))
    return "".join(encode)

text = input("Введите строку: ")
print("Закодированная строка:", encode(text))
"""


