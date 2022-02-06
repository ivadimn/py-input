"""
class X:
    pass

class A(X):
    pass

class B(X):
    pass

class C(X):
    pass

class D(X):
    pass


class E(A, B):
    pass

class F(B, C):
    pass

class G(B, C, D):
    pass

class H(C, D):
    pass

class J(E, G):
    pass

class K(F, G, H):
    pass

class Z(J, K):
    pass


z = Z()
print(z.__class__.__mro__)
"""

class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return "Я - робот, модель: {model}".format(model=self.model)

class CanFly:
    def __init__(self, speed = 0, height = 0):
        self.speed = speed
        self.height = height

    def fly_in(self, speed, height):
        print("Взлетел...")
        self.speed = speed
        self.height = height

    def flying(self):
        print("Лечу .. скорость: {speed} высота: {height}".format(speed=self.speed, height=self.height))

    def to_land(self):
        print("Приземлился...")
        self.speed = 0
        self.height = 0

    def __str__(self):
        print("Я могу летать...")


class Dron(Robot, CanFly):
     def __init__(self, model):
         super().__init__(model)

     def operate(self):
         print("Веду разведку с воздуха")
         self.flying()


class WarRobot(Robot, CanFly):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print("Защищаю военный объект с воздуха с помощью {gun}".format(gun = self.gun))
       