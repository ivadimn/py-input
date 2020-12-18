
from random import randint, choice


class Player:
    health = 10
    max_health = 10
    position = []

    # добавлено для создании позиции игрока случайным образом
    def __init__(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        self.position = [randint(0, map_width - 1), randint(0, map_height - 1)] # пока карта пустая можно вставлять куда угодно

    def was_hit(self, hid):
        self.health -= choice(range(hid + 1))


    def wait(self):
        if self.health < self.max_health:
            self.health += 1
        print("player's health: ", self.health)