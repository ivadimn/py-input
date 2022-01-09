"""
class Toyota:

    def __init__(self, color, price, max_speed, current_speed = 0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print("Color: {0}\nPrice: {1}\nMax. speed: {2}\nCurrent speed: {3}\n".format(self.color,
                                                     self.price, self.max_speed, self.current_speed))

    def set_current_speed(self, speed):
        self.current_speed = speed
        print("Установлена скорость {0} км/ч.\n".format(self.current_speed))

car = Toyota("White", 1500000, 250)
car.info()
car.set_current_speed(120)
car.info()


class Point:
    count = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.count += 1


p1 = Point()
p2 = Point(10, 20)
print(Point.count)
"""

class Potato:
    states =  {0: "Неизвестно", 1: "Росток", 2: "Зелёная", 3: "Зрелая"}

    def __init__(self, index, state = 0):
        self.index = index
        self.state = state

    def print_state(self):
        print("Картошка {0} сейчас {1}".format(self.index, self.states[self.state]))

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        return self.state == 3

class GardenPotato():

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(4)]

    def graw_all(self):
        print("Картошка прорастает!")
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print("Картошка ещё не созрела")
        else:
            print("Картошка уже созрела можно собирать")

my_graden = GardenPotato(5)
my_graden.are_all_ripe()
for _ in range(3):
    my_graden.graw_all()
    my_graden.are_all_ripe()