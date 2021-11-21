"""
zoo = ["lion", "kangaroo", "elephant", "monkey"]
zoo.insert(1, "bear")
print(zoo)
print("Лев сидит в клетке номер", zoo.index("lion") + 1)
print("Обезьяна сидит в клетке номер", zoo.index("monkey") + 1)


count_person = int(input("Кол-во сотрудников: "))
list_person = []
for i in range(count_person):
    print("Зарплата", i + 1, "сотрудника: ", end = "")
    list_person.append(int(input()))
while 0 in list_person:
    list_person.remove(0)
print("Осталось сотрудников:", len(list_person))
print("Зарплаты:", list_person)

print("Максимальная зарплать: ", max(list_person))
print("Минимальная зарплать: ", min(list_person))
"""

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица']

my_list = []
while True:
    print("Ваш текущий топ фильмов:", my_list)
    film = input("Название фильма: ")
    if film in films:
        print("Команды: добавить, вставить, удалить")
        command = input("Введите команду: ")
        if command == "добавить":
            if not (film in my_list):
                my_list.append(film)
        elif command == "удалить":
            if film in my_list:
                my_list.remove(film)
        elif command == "вставить":
            pos = int(input("В какое место вставляем? "))
            my_list.insert(pos - 1, film)
    else:
        print("Такого фильма нет на сайте.")