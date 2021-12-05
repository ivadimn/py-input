"""
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789!?.,:;-"

def encrypt(message, key):
    encrypted_message = ""
    for ch in message:
        if ch in alphabet:
            index = alphabet.find(ch)
            new_index = index + key
            if new_index >= len(alphabet):
                new_index -= len(alphabet)
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += ch
    return encrypted_message


def encrypt1(message, key):
    encrypted_message = [alphabet[(alphabet.find(ch) + key) % len(alphabet)] if ch in alphabet else ch for ch in message]
    return "".join(encrypted_message)

message = input("Введите сообщение: ").lower()
shift = int(input("Введите сдвиг: "))
print("Зашифрованное сообщение:", encrypt1(message, shift))


path = input("Путь к файлу: ")
disk = input("На каком диске должен лежать файл: ")
ext = input("Требуемое расширение файла: ")
if not path.startswith(disk):
    print("Ошибка: Неверно указан диск!")
elif not path.endswith(ext):
    print("Ошибка: Неверно указано расширение!")
else:
    print("Путь корректен!")
"""

text = input("Введите строку: ")
count_upper = 0
count_lower = 0
for ch in text:
    if ch.islower():
        count_lower += 1
    else:
        count_upper += 1

if count_lower > count_upper:
    print("Результат:", text.lower())
else:
    print("Результат:", text.upper())
