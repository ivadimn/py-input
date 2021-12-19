import random

"""
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    return ([(key, val["age"]) for key, val in students.items()],
        [interest for key, val in students.items() for interest in val.get("interests", [])],
        len("".join([val.get("surname", "") for key, val in students.items()])))

ages, interests, surnames_len = f(students)

print('Список пар "ID студента - Возраст" {0}'.format(ages))
print("Список всех интересрв: {0}".format(interests))
print("Суммарная длина всех фамилий: {0}".format(surnames_len))


def is_prime(num: int):
    if num < 2:
        return False
    l_num = num - 1
    while l_num > 1:
        if num % l_num == 0:
            return False
        l_num -= 1
    return True

def create_list(iter_obj):
    return [{obj : iter_obj[obj]} if isinstance(iter_obj, dict) else obj for i, obj in enumerate(iter_obj) if is_prime(i)]


line = "какая то строка"
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
d = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}
print(create_list(line))
print(create_list(t))
print(create_list(d))



def get_new_tuple(t: tuple, num: int):
    if t.count(num) == 0:
        return ()
    f_index = t.index(num)
    if t.count(num) == 1:
        return t[f_index:]
    else:
        s_index = t.index(num, f_index + 1)
        return t[f_index:s_index + 1]

t = (1, 2, 3, 4, 5, 6, 7, 3, 9, 10)
print(get_new_tuple(t, 3))
print(get_new_tuple(t, 4))
print(get_new_tuple(t, 20))


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
l = [key + val for key, val in players.items()]
print(l)


familys = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Иванов", "Петр"): 55,
    ("Иванова", "Анна"): 54,
    ("Иванов", "Андрей"): 30
}

surname = input("Введите фамилию: ").capitalize()
if surname[-1] == "а":
    surname = surname[:-1]
for key,val in familys.items():
    if surname in key[0]:
        print("{0} {1} {2}".format(key[0], key[1], val))


origin = [random.randint(0, 15) for _ in range(10)]
print("Оригинальный список: ", origin)
new_list1 = [(origin[i], origin[i + 1]) for i in range(0, len(origin), 2)]
print("Новый список 1: ", new_list1)
new_list2 = [(origin[i * 2], origin[i * 2 + 1]) for i in range(len(origin) // 2)]
print("Новый список 1: ", new_list2)
new_list3 = list(zip(origin[::2], origin[1::2]))
print("Новый список 2: ", new_list3)

def bubble_sort(arr):
    if not isinstance(sum(arr), int):
        return arr
    sorted_arr = list(arr)
    for i in range(len(sorted_arr)):
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[j] < sorted_arr[i]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
    return tuple(sorted_arr)

print(bubble_sort((10, 12, 8, 90, 6, 0, 4, 3, 1)))
print(bubble_sort((10, 12, 8.091, 90, 6, 0, 4, 3, 1)))


phone_book = dict()
while True:
    print("\nЧто будем делать?")
    print(" 1. Добавитьконтакт.")
    print(" 2. Поиск человека по фамилии.")
    command = int(input(">: "))
    if command == 1:
        contact = input("Введите Фамилию Имя и телефон через пробел: ").split()
        name = (contact[0].capitalize(), contact[1].capitalize())
        if name in phone_book:
            print("Такой контакт уже есть в телефонной книге!")
        else:
            phone_book[name] = int(contact[2])re
            print(phone_book)
    elif command == 2:
        surname = input("Введите Фамилию: ").capitalize()
        contacts = [(key[0], key[1], val) for key, val in phone_book.items() if surname in key]
        print("Найденные контакты: {0}\n".format(contacts))
    else:
        print("Не правильная команда!")
        break
"""

protokol = {
    "Jack" : (69485, 0),
    "qwerty" : (197128, 4),
    "Jack" : (95715, 5),
    "Alex" : (95715, 3),
    "M" : (95715, 8),
}
#numr = int(input("Сколько записей вносится в протокол? "))
#for i in range(numr):
#    record = input("{0} запись: ".format(i + 1)).split()
#    if record[1] in protokol:
#        if protokol[record[1]][0] < int(record[0]):
#            protokol[record[1]] = (int(record[0]), i)
#    else:
#        protokol[record[1]] = (int(record[0]), i)

print(sorted(protokol, key=lambda name:  protokol[name][0] + (9 - protokol[name][1]), reverse=True))

