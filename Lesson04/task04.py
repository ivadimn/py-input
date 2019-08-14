# 4:Давайте усложним предыдущее задание. Измените сущности,
# добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
def get_damage(attacking, attacked):
    return attacking["damage"] / attacked["armor"]


def attack(attacking, attacked):
    attacked["health"] = attacked["health"] - get_damage(attacking, attacked)


player = {"name": "", "health": 100, "damage": 50, "armor": 1.2}
enemy = {"name": "", "health": 100, "damage": 50, "armor": 1.2}


player["name"] = input("Введите имя атакующего: ")
enemy["name"] = input("Введите имя атакуемого: ")

attack(player, enemy)
print(player)
print(enemy)