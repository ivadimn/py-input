class Unit:

    def __init__(self, health):
        self.health = health

    def damage(self, damag = 0):
        self.health -= damag


class Solder(Unit):

    def __init__(self, health):
        super().__init__(health)

    def damage(self, damag = 0):
        super().damage()
        self.health -= damag


class Man(Unit):

    def __init__(self, health):
        super().__init__(health)

    def damage(self, damag = 0):
        super().damage()
        self.health -= damag * 2


class CanFly:
    height = 0
    speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def to_land(self):
        self.height = 0
        self.speed = 0

    def info(self):
        print("Высота: {0}, скорость: {1}".format(self.height, self.speed))

class Butterfly(CanFly):

    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):

    def take_off(self):
        self.height = 500
        self.speed = 1000

    def fly(self):
        self.speed = 0.5

    def to_land(self):
        super().to_land()

    def buuh(self):
        print("Ракета взорвалась")
