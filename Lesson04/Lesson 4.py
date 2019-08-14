# 1: Создайте функцию, принимающую на вход имя, возраст
# и город проживания человека. Функция должна возвращать строку
# вида «Василий, 21 год(а),
# проживает в городе Москва»

def person (name, age, from_in):
    enter = (name + ", " + age + " год(а)," + " проживает в городе " + from_in)
    return enter
name = input("Введите имя: ")
age = input("Введите возраст: ")
from_in = input("Введите город проживания: ")

print(person(name, age, from_in))

# 2: Создайте функцию, принимающую на вход 3 числа
# и возвращающую наибольшее из них.

def m(a, b, c):
    list = [a, b, c]
    return max(list)
a = float(input("Введите 1-ое число: "))
b = float(input("Введите 2-ое число: "))
c = float(input("Введите 3-е число: "))
print (m(a, b, c))


# 3: Давайте опишем пару сущностей player и
# enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и
# жизней по желанию. ### Теперь надо создать функцию
# attack(person1, person2). Примечание: имена аргументов
# можете указать свои. ### Функция в качестве аргумента
# будет принимать атакующего и атакуемого. ### В теле
# функция должна получить параметр damage атакующего и
# отнять это количество от health атакуемого. Функция
# должна сама работать со словарями и изменять их значения.

name_player = input("Введите имя игрока: ")
name_enemy = input("Введите имя противника: ")

player = {"name": name_player, "healf":100, "damage":50}
enemy = {"name": name_enemy, "healf":100, "damage":50}

def attack(person1, person2):
        person1["healf"] -= person2["damage"]

attacker = int(input(f"Если атакует {name_player} - нажмите '1', если атакует {name_enemy} - '2': "))
if attacker == 1:
    attack(enemy,player)
else:
    attack(player, enemy)

print(player)
print(enemy)






# 4: Давайте усложним предыдущее задание. Измените сущности,
# добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять
# и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции
# номер 1 для вычисления урона и вычитания его из здоровья персонажа.

name_player = input("Введите имя игрока: ")
name_enemy = input("Введите имя противника: ")

player = {"name": name_player, "healf":100, "damage":50, "armour":1.2}
enemy = {"name": name_enemy, "healf":100, "damage":50, "armour":1.3}

def attack(person1, person2):
        person1["healf"] -= arm(person1, person2)
def arm(person1, person2):
    k = person2["damage"]/person1["armour"]
    return k
round = 0
while player["healf"]*enemy["healf"]>0:
    round += 1
    print("Раунд ", round, ":")
    attacker = int(input(f"Если атакует {name_player} - нажмите '1', если атакует {name_enemy} - '2': "))
    if attacker == 1:
        attack(enemy,player)
        print(f"Здоровье {name_player}:", player["healf"])
        print(f"Здоровье {name_enemy}:", enemy["healf"])
    else:
        attack(player, enemy)
        print(f"Здоровье {name_player}:", player["healf"])
        print(f"Здоровье {name_enemy}:", enemy["healf"])
if player["healf"] <= 0:
    print(f"{name_player} проиграл!")
if enemy["healf"] <= 0:
    print(f"{name_enemy} проиграл!")

