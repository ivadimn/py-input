class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return "Корабль модель: {}".format(self.model)

    def sail(self):
        print("корабль {} поплыл куда - то".format(self.model))


class WarShip(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print("Корабль {0} атакует с помощью {1}".format(self.model, self.gun))


class CargoShip(Ship):

    def __init__(self, model, tonnage = 0):
        super().__init__(model)
        self.tonnage = tonnage

    def load(self):
        print("Грузим на корабль {0}".format(self.model))
        self.tonnage += 1
        print("Уже загружено {0}".format(self.tonnage))

    def unload(self):
        print("Выгружаем с корабля {0}".format(self.model))
        self.tonnage -= 1
        print("Осталось {0}".format(self.tonnage))


ws = WarShip("Linkor01", "Пушки")
ws.sail()
ws.attack()


class Robot:

    def __init__(self, model):
        self.model = model

    def operate(self):
        pass


class VacuumRobot(Robot):

    def __init__(self, model, bag = 0):
        super().__init__(model)
        self.bag = bag

    def operate(self):
        super().operate()
        print("Пылесос пылесосит")
        self.bag += 1
        print("Текущая наполненность мешка {0}".format(self.bag))


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print("Робот {0} защищает объект с помощью {1}".format(self.model, self.gun))


class SubMarineRobot(WarRobot):

    def __init__(self, model, gun, deep):
        super().__init__(model, gun)
        self.deep = deep

    def operate(self):
        super().operate()
        print("Охрана ведётся под водой!")


va = VacuumRobot("VacuumCleaner")
va.operate()

sub = SubMarineRobot("K119", "Торпеды", 50)
sub.operate()


class DivisionException(Exception):
    pass


with open("numbers.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.split()))
        if nums[0] < nums[1]:
            raise DivisionException("Нельзя делить меньшее число на большее")
        else:
            print(nums[0] / nums[1])

