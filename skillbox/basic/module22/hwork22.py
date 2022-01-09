"""
file = open("numbers.txt", "r")
summ = 0
for num in file:
    summ += int(num.strip())
file.close()

out_file = open("summ.txt", "w")
out_file.write(str(summ))
out_file.close()
"""

import os

"""
path = os.path.join("..", "02_zen_of_python", "zen.txt")
table1 = "".maketrans("-+/!?,:&%$##@*.'", "                ")

file = open(path, "r")
lines = list(file)
count_lines = len(lines)
words = " ".join(lines).translate(table1).split()
count_words = len(words)
symbols = "".join(words)
count_symbols = len(symbols)
freq = {ch : symbols.count(ch) for ch in set(symbols)}
freq_sorted = sorted(freq, key=freq.get)

print("Количество строк в файле: {0}".format(count_lines))
print("Количество слов в файле: {0}".format(count_words))
print("Количество букв в файле: {0}".format(count_symbols))
print("Буква {0} встречается в тексте наименьшее количество раз - {1}.".format(freq_sorted[0], freq[freq_sorted[0]]))
file.close()


def dir_info(cur_path):
    info = {"files": 0, "folders": 0, "size": 0}
    if not os.path.exists(cur_path):
        print("Каталог {0} отсутствует!".format(cur_path))
        return info
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if os.path.isdir(path):
            info["folders"] += 1
            inf = dir_info(path)
            for k in info:
                info[k] += inf[k]
        else:
            info["files"] += 1
            info["size"] += os.path.getsize(path)
    return info

path = input("Введите путь к папке: ")
info = dir_info(path)
print("Размер каталога (в Кб): {0}".format(info["size"] / 1024))
print("Количество подкаталогов: {0}".format(info["folders"]))
print("Количество файлов: {}".format(info["files"]))


def get_path():
    while True:
        folders = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ").split()
        path = os.path.abspath(os.path.join(*folders))
        if os.path.exists(path):
            return path
        else:
            abs_path = os.path.abspath(os.path.join(os.path.sep, *folders))
            if os.path.exists(abs_path):
                return abs_path
            else:
                print("Введённый путь не существует, попробуйте ещё раз!")


def write_file(fpath, text):
    file = open(file_path, "w")
    file.write(text)
    file.close()


text = input("Введите строку: ")
path = get_path()
file_name = input("Введите имя файла: ")
file_path = os.path.join(path, file_name)
if os.path.exists(file_path):
    answer = input("Вы действительно хотите перезаписать файл? ")
    if answer == "да":
        write_file(file_path, text)
        print("Файл успешно перезаписан!")
else:
    write_file(file_path, text)
    print("Файл успешно сохранён!")


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?.,:;-"

def shift(l, k):
    l_new = l.copy()
    len_list = len(l)
    for i in range(len_list):
        i_new = (i + k) % len_list
        l_new[i_new] = l[i]
    return l_new

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



file = open("text.txt", "r")
encrypt_file = open("cipher_text.txt", "w")
print("Содержимое файла text.txt:")
for i, line in enumerate(list(file)):
    print(line, end = "")
    encrypt_line = encrypt(line, i + 1)
    encrypt_file.write(encrypt_line)
file.close()
encrypt_file.close()

encrypt_file = open("cipher_text.txt", "r")
print("\nСодержимое файла cipher_text.txt:")
for line in encrypt_file:
    print(line, end = "")
encrypt_file.close()


first_tour_file = open("first_tour.txt")
score = int(first_tour_file.readline())
second_tour_members = dict()
print("Содержимое файла first_tour.txt:")
print(score)
for line in first_tour_file:
    print(line, end = "")
    member = line.split()
    if int(member[2]) > score:
        key = "{0}. {1}".format(member[1][0], member[0])
        second_tour_members[key] = int(member[2])
first_tour_file.close()

sorted_keys = sorted(second_tour_members, key = second_tour_members.get, reverse = True)
second_tour_file = open("second_tour.txt", "w")
for i, k in enumerate(sorted_keys):
    second_tour_file.write("{0}) {1} {2}\n".format(i + 1, k, second_tour_members[k]))
second_tour_file.close()

print("\n\nСодержимое файла second_tour.txt:")
second_tour_file = open("second_tour.txt", "r")
for line in second_tour_file:
    print(line, end = "")
second_tour_file.close()
"""


table1 = "".maketrans("", "", " -+/!?,:&%$##@*.'\n")
file = open("text.txt", "r")
text = file.read()
file.close()
print("Содержание файла text.txt: ")
print(text)
symbols = text.translate(table1).lower()
text_len = len(symbols)
freq = {ch : round(text.count(ch) / text_len, 3) for ch in sorted(set(symbols))}
freq_sorted = {key : freq[key] for key in sorted(freq, key=freq.get, reverse = True)}
file = open("analysis.txt", "w")
print("\nСодержание файла analysis.txt:")
for key, val in freq_sorted.items():
    line = "{0} {1}\n".format(key, str(val))
    print(line, end = "")
    file.write(line)
file.close()



