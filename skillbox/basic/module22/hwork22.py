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
path = os.path.join("..", "02_zen_of_python", "zen.txt")
table1 = "".maketrans("-+/!?,:&%$##@*.'", "                ")
"""
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
"""

def dir_info(cur_path):
    info = {"files": 0, "folders": 0, "size": 0}
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
print(info)