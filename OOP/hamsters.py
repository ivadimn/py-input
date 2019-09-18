from random import randint


class Hamster:
    position = [0, 0]
    health = 3

    def __init__(self, hid, map_width, map_height):
        self.id = hid
        self.health = randint(1, 4)
        self.position = [randint(0, map_width - 1), randint(0, map_height - 1)]