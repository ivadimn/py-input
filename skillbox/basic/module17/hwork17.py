import random
"""
vowels = "уеыаоэяию"
text = input("Введите текст: ")

list_vowels = [ch for ch in text if ch.lower() in vowels]
print("Список гласных букв:", list_vowels)
print("Длина списка:", len(list_vowels))


count_nums = int(input("Введите длину списка: "))
list_nums = [1 if n % 2 == 0 else n % 5 for n in range(count_nums)]
print("Результат:", list_nums)


count_members = 20
team1 = [round(random.uniform(5, 10), 2) for _ in range(count_members)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(count_members)]
list_winners = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(count_members)]

print("Первая команда:", team1)
print("Вторая команда:", team2)
print("Победители тура:", list_winners)


alphabet = "abcdefg"
print("1. Копия:", alphabet[:])
print("2. Элементы строки в обратном порядке:", alphabet[::-1])
print("3. Каждый второй элемент строки (включая самый первый):", alphabet[::2])
print("4. Каждый второй элемент строки после первого:", alphabet[1::2])
print("5. Все элементы до второго:", alphabet[:1])
print("6. Все элементы, начаная с конца до предпоследнего:", alphabet[-1:])
print("7. Все элементы в диапазоне индексов от 3 до 4 (не включая 4):", alphabet[3:4])
print("8. Последние три элемента строки:", alphabet[-3:])
print("9. Все элементы в диапазоне индексов от 3 до 4 (не включая 5):", alphabet[3:5])
print("10. То же, что и в предыдущем пункте, но в обратном порядке:", alphabet[-3:-5:-1])


line = input("Введите строку как минимум с думя буквами <h>: ")
index1 = line.lower().index("h")
index2 = line.lower().index("h", index1 + 1)
sub_line = line[index1+1: index2]
print("Перевёрнутая строка между двумя <h>:", sub_line[::-1])
print(line[:index1 + 1] + sub_line[::-1] + line[index2:])


list_num = list(map(int, input("Введите целые числа через пробел: ").split(" ")))
print("Исхолный список:", list_num)
count_zero = list_num.count(0)
for _ in range(count_zero):
    list_num.remove(0)
    list_num.append(0)
index_zero = list_num.index(0)
list_num[index_zero:] = []
print("Список без нулей:", list_num)


array = [[j + (i * 4)   for i in range(3) ] for j in range(1, 5)]
print(array)

count_sticks = int(input("Количество палок: "))
count_throws = int(input("Количество бросков: "))
list_sticks = list("|" * count_sticks)

for i in range(1, count_throws + 1):
    print("Бросок", i, "Сбиты палки с номера ", end = "")
    begin = int(input())
    end = int(input("по номер "))
    list_sticks[begin - 1:end] = ["." for _ in range(end - begin + 1)]
print("Результат:", "".join(list_sticks))
"""

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
nice_list1 = [nice_list[i // 10][i // 6][i // 6]  for i in range(18)]
print(nice_list1)
