def questions(name, age, city):
    print("{}, {} год(а), проживает в городе {}".format(name, age, city))

print("ЗАДАНИЕ 1")

name = input("Имя: ")
age = input("Возраст: ")
city = input("Город: ")

questions(name, age, city)

print("##############################")


def max_num(num_1, num_2, num_3):
    print("Самое большое число: ", max(num_1, num_2, num_3))

print("ЗАДАНИЕ 2")

num1 = input("Первое число: ")
num2 = input("Второе число: ")
num3 = input("Третье число: ")
print(num1, num2, num3)

max_num(num1, num2, num3)

print("##############################")
def add(dictionary):
    """Функция, которая нужна для того, чтобы не дублировать значения health, damage и armor для player и enemy"""
    dictionary["health"] = 100.0
    dictionary["damage"] = 50.0
    dictionary["armor"] = 1.2

def attack(person_1, person_2):
    """person_1 - это атакующий, person_2 - атакуемый"""
    global damage
    def arm():
        global damage
        damage /= person_2["armor"]

    person_1_name, person_2_name = person_1["name"], person_2["name"]
    damage = person_1["damage"]
    health = person_2["health"]

    arm()

    health -= damage
    person_2["health"] = health
    print(person_1_name, " атаковал ", person_2_name, " и нанес ему ", damage, " урона. У ", person_2_name, " осталось ", health, " здоровья.", sep='')

print("ЗАДАНИЕ 3")

player_name = input("Имя игрока: ")
enemy_name = input("Имя врага: ")

player = { "name": player_name }
enemy = { "name": enemy_name }

add(player)
add(enemy)

attack(player, enemy)




