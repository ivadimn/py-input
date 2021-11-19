"""
number = int(input("Введите число: "))
odd_list = [n for n in range(1, number + 1) if n % 2 != 0]
print(odd_list)


names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
for index in range(len(names)):
    if index % 2 == 0:
        print("Индекс:", index, ", имя:", names[index])


count_cages = int(input("Кол-во клеток: "))
cages_list = []
for i in range(count_cages):
    print("Эффективность", i + 1, "клетки: ", end = "")
    cages_list.append(int(input()))
print("\nНеподходящие знвчения: ", end = "")
for index in range(len(cages_list)):
    if cages_list[index] < index + 1:
        print(cages_list[index], end = " ")
print()


def get_max(l):
    max_value = l[0]
    for e in l:
        if e > max_value:
            max_value = e
    return max_value

count_videos = int(input("Кол-во вилеокапт: "))
videos_list = []
for i in range(count_videos):
    print(i + 1, "Видеокарта: ", end = "")
    videos_list.append(int(input()))

max_video = get_max(videos_list)
new_list = [ v for v in videos_list if v < max_video]

print("\nСтарый список видеокарт: ", videos_list)
print("Новый список видеокарт: ", new_list)


films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"]
favorites = []
film = input("Введите фильм: ")
while film != "end":
    if film in films and film not in favorites :
        favorites.append(film)
    else:
        print("Ошибка!!!")
    film = input("Введите фильм: ")
print("Любимые фильмы: ", favorites)

def get_count(l, ch):
    count = 0
    for c in l:
        if c == ch:
            count += 1
    return count

uniq_count = 0
ch_list = list(input("Введите слово: "))
for ch in ch_list:
    if get_count(ch_list, ch) == 1:
        uniq_count += 1
print("Кол-во уникальных букв:", uniq_count)


def get_weight():
    weight = int(input("ведите вес контейнера (<=200): "))
    while weight > 200:
        print("Вес контейнера должен быть не более 200, попробуйте ещё: ", end = "")
        weight = int(input())
    return weight

count_сcontainers = int(input("Кол-во контейнеров: "))
containers_list = []
for i in range(count_сcontainers):
    containers_list.append(get_weight())

new_container = int(input("Введите вес нового контейнера: "))
insert_index = 0
min_r = 200
for i in range(len(containers_list)):
    r = new_container - containers_list[i]
    if r >= 0 and r <= min_r:
        min_r = r
        insert_index = i
print(insert_index)


def shift(l, k):
    l_new = l.copy()
    len_list = len(l)
    for i in range(len_list):
        i_new = i + k
        if i_new >= len_list:
            i_new -= len_list
        l_new[i_new] = l[i]
    return l_new

list_numbers = list(map(int, input("Введите числа через пробел: ").split(" ")))
k = int(input("Сдвиг: "))
print("Изначальный список:", list_numbers)
print("Сдвинутый список список:", shift(list_numbers, k))


def reverse(l):
    l_r = l.copy()
    len_list = len(l)
    for i in range(len_list // 2):
        l_r[i], l_r[len_list - i - 1] = l_r[len_list - i - 1], l_r[i]
    return l_r

word = list(input("Введите слово: "))
if word == reverse(word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
"""

l = [10,3, 8, 0, 27, 99 ,1 -10]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] < l[i]:
            l[i], l[j] = l[j], l[i]
print(l)




