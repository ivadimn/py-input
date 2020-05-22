# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

import hashlib

s = input("Введите строку для посчёта подстрок : ")
assert len(s) > 0, "Пустая строка!!"

hash_subs = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        ss = s[i:j]
        if (ss != s):
            print(f"Подстрока - {ss}")
            hash_subs.add(hashlib.sha1(ss.encode("utf-8")).hexdigest())
print("*" * 40)
print(f"Количество различных подстрок  введённой строки {len(hash_subs)}")
print("*" * 40)
print("Хэши подстрок : ")
for hash in hash_subs:
    print(hash)
