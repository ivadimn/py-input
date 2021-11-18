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
"""

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