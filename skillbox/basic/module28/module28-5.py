from abc import ABC, abstractmethod

class Transport(ABC):

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

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