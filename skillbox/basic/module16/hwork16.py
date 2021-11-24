"""
def remove_elems(l : list, e):
    while e in l:
        l.remove(e)
    return l

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print("Кол-во цифр 5 при первом объединении:", a.count(5))
a = remove_elems(a, 5)
a.extend(c)
print("Кол-во цифр 3 при втором объединении:", a.count(3))
print("Итоговый список:", a)


puple_list1 = list(range(160, 177, 2))
puple_list2 = list(range(162, 181, 3))
puple_list1.extend(puple_list2)
puple_list1.sort()
print("Список:", puple_list1)


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
name = input("Название детали: ")
count = 0
summ = 0
for detail in shop:
    if detail[0] == name:
        count += 1
        summ += detail[1]
print("Кол-во деталей -", count)
print("Общая стоимость -", summ)


guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
command = ""
while True:
    print("Сейчас на вечеринке",  len(guests),  "человек:", guests)
    command = input("Гость пришёл или ушёл? ")
    if command == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    name = input("Имя гостя: ")
    if command == "пришёл":
        if len(guests) == 6:
            print("Прости,", name, ", но мест нет.")
        else:
            print("Привет,", name, "!")
            guests.append(name)
    elif command == "ушёл" and name in guests:
        guests.remove(name)
        print("Пока,", name, "!")


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

def get_song_duration(song, l_songs):
    duration = 0
    for s in l_songs:
        if s[0] == song:
            duration = s[1]
    return duration


count_songs = int(input("Сколько песен выбрать? "))
common_time = 0
for i in range(count_songs):
    print("Название", i + 1, "песни: ", end = "")
    song = input()
    common_time += get_song_duration(song, violator_songs)
print("Общее время звучания песен:", round(common_time, 2), "минут")


list_1 = list(map(int, input("Введите 3 числа через пробел: ").split(" ")))
list_2 = list(map(int, input("Введите 7 чисел через пробел: ").split(" ")))

print("Первый список:", list_1)
print("Второй список:", list_2)
list_1.extend(list_2)
for e in list_1:
    for _ in range(list_1.count(e) - 1):
        list_1.remove(e)

print("Новый первый список с уникальными элементами:", list_1)


list_skates = []
list_man = []
count_skates = int(input("Кол-во коньков: "))
for i in range(count_skates):
    print("Размер", i + 1, "пары: ", end = "")
    list_skates.append(int(input()))

count_man = int(input("\nКол-во людей: "))
for i in range(count_man):
    print("Размер ноги", i + 1, "человека: ", end = "")
    list_man.append(int(input()))

max_count_man = 0
for size in list_man:
    if size in list_skates:
        max_count_man += 1
        list_skates.remove(size)
print("\nНаибольшее кол-во людей, которые могут взять ролики:", max_count_man)


count_man = int(input("Кол-во человек: "))
num = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", num,  "человек")
list_man = list(range(1, count_man + 1))
begin = 1
index = list_man.index(begin)
while len(list_man) > 1:
    l = len(list_man)
    print("\nTекущий круг людей:", list_man)
    print("Начало счёта с номера", list_man[index])
    if num > l:
        c = num // l
        index += num - (l * c) - 1
    elif num <= l:
        index += num - 1
        if index >= l:
            index -= l
    value = list_man[index]
    list_man.remove(value)
    print("Выбывает человек под номером", value)
    if index >= len(list_man):
        index = 0
print("\nОстался человек под номером", list_man[0])
"""

count_friends = int(input("Кол-во друзей: "))
iou_count = int(input("Долговых расписок: "))
iou_list = []
for i in range(iou_count):
    print(i + 1, "расписка")
    t = int(input("Кому: "))
    f = int(input("От кого: "))
    how_much = int(input("Сколько: "))
    iou_list.append([t, f, how_much])
