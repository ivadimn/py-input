from abc import ABC, abstractmethod

"""
class Transport(ABC):

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def beep(self):
        pass


class MusicPlayerMixin:
    @abstractmethod
    def play(self):
        print("Играет музыка!!")

class Car(Transport):

    def __init__(self, speed, color):
        super().__init__(speed, color)

    def move(self):
        print("Автомобиль едет со скоростью {speed} км/ч.".format(speed=self.speed))

    def beep(self):
        print("{color} автомобиль подал сигнал!!".format(color=self.color))


class Boat(Transport):
    def __init__(self, speed, color):
        super().__init__(speed, color)

    def move(self):
        print("Лодка плывет со скоростью {speed} км/ч.".format(speed=self.speed))

    def beep(self):
        print("{color} лодка подала сигнал!!".format(color=self.color))


class Amphibian(Transport, MusicPlayerMixin):

    def __init__(self, speed, color):
        super().__init__(speed, color)

    def move(self):
        print("Анфибия плывет и едет со скоростью {speed} км/ч.".format(speed=self.speed))

    def beep(self):
        print("{color} анфибия подала сигнал!!".format(color=self.color))

    def play(self):
        print("В анфибии играет музыка!!")


car = Car(200, "Красный")
boat = Boat(50, "Белая")
anf = Amphibian(155, "Голубая")

for tr in [car, boat, anf]:
    tr.move()
    tr.beep()
"""


class ResizebleMixin(ABC):
    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width


class Figure(ABC):

    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Rect(Figure, ResizebleMixin):
    pass


class Square(Figure, ResizebleMixin):

    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)


r1 = Rect(1, 3, 5, 10)
r2 = Rect(2, 4, 10, 15)
s1 = Square(4, 4, 4)

for fig in [r1, r2, s1]:
    new_length = fig.length * 2
    new_width = fig.width * 2
    fig.resize(new_length, new_width)