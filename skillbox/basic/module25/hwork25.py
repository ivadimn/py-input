import random
import math

"""
class Property:

    def __init__(self, worth):
        self.worth = worth

    def calc_tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.tax_rate = 1 / 1000

    def calc_tax(self):
        return round(self.worth * self.tax_rate, 2)

    def __str__(self):
        return "Квартира"


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.tax_rate = 1 / 200

    def calc_tax(self):
        return round(self.worth * self.tax_rate, 2)

    def __str__(self):
        return "Машина"


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.tax_rate = 1 / 500

    def calc_tax(self):
        return round(self.worth * self.tax_rate, 2)

    def __str__(self):
        return "Дача"


money = int(input("Сколько у вас денег? "))
property = []
worth_apartment = int(input("Сколько стоит квартира? "))
property.append(Apartment(worth_apartment))
worth_car = int(input("Сколько стоит машина? "))
property.append(Car(worth_car))
worth_dacha = int(input("Сколько стоит дача? "))
property.append(CountryHouse(worth_dacha))

tax_summa = 0
for prop in property:
    tax = prop.calc_tax()
    print("Налог на {0} составляет: {1}".format(prop, tax))
    tax_summa += tax

print("\nСуммарный налог на имущество составляет {0}".format(tax_summa))
if tax_summa > money:
    print("Вам не хватает для уплаты налога: {}".format(tax_summa - money))


class KillError(Exception):
    def __init__(self):
        super().__init__("Вас убили!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Сегодня вы пьяны!")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в автомобильную катaстрофу!")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы переели!")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("У вас депрессия!")

class Karma:
    __chance = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    __exceptions = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]

    def __init__(self):
        self.karma = 0

    def __probability(self):
        return self.__chance[random.randint(0, 9)]


    def one_day(self):
        prob = self.__probability()
        if prob == 1:
            raise self.__exceptions[random.randint(0, 4)]
        self.karma += random.randint(1, 7)

def write_karma_log(error : str):
    with open("karma.log", "a") as log_file:
        log_file.write("{}\n".format(error))


max_karma = 500
karma = Karma()
while karma.karma < 500:
    try:
        karma.one_day()
    except Exception as ex:
        write_karma_log(ex.args[0])

print("Вы в нирване у вас карма {0}".format(karma.karma))


class MyDict(dict):

    def get(self, key):
        val = super().get(key)
        if val is None:
            val = 0
        return val


my_dict = MyDict()
d = {"0": 0, "1": 1, "2": 2, "3": 1}
my_dict.update(d)
print(d.get(10))
print(my_dict.get(10))


class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return "Имя: {0}, Фамилия: {1}, Возраст: {2}".format(self.__name, self.__surname, self.__age)

class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calc_salary(self):
        pass

class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calc_salary(self):
        return 13000

    def __str__(self):
        name = super().__str__()
        return " ".join(("Менеджер", name))


class Agent(Employee):

    def __init__(self, name, surname, age, sales = 0):
        super().__init__(name, surname, age)
        self.sales = sales

    def calc_salary(self):
        return 5000 + self.sales * 0.05

    def __str__(self):
        name = super().__str__()
        return " ".join(("Агент", name))

class Worker(Employee):

    def __init__(self, name, surname, age, hours=0):
        super().__init__(name, surname, age)
        self.hours = hours

    def calc_salary(self):
        return 100 * self.hours

    def __str__(self):
        name = super().__str__()
        return " ".join(("Рабочий", name))


employees =  [Manager("Вася", "Иванов", 40), Manager("Петя", "Сидоров", 25), Manager("Аня", "Петрова", 35),
              Agent("Андрей", "Васильев", 35, 20000), Agent("Миша", "Федоров", 35, 30000),
              Agent("Сергей", "Семенов", 25, 50000),
              Worker("Леша", "Комаров", 25, 50), Worker("Саша", "Иванов", 50, 120), Worker("Федя", "Петров", 20, 40)
              ]

for emp in employees:
    print("\n{0}\nЗарплата: {1}".format(emp, emp.calc_salary()))
"""


class Car:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance):
        delta_x = distance * math.cos(math.radians(self.angle))
        delta_y = distance * math.sin(math.radians(self.angle))
        self.x += delta_x
        self.y += delta_y

    def to_turn(self, new_angle):
        self.angle = new_angle

    def __str__(self):
        return "(Координаты: {0}, {1}), направление {2} градусов".format(self.x, self.y, self.angle)


class Bus(Car):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.money = 0
        self.passengers = 0

    def come_in(self, count):
        self.passengers += count

    def get_off(self, count):
        if self.passengers >= count:
            self.passengers -= count
        else:
            self.passengers = 0

    def move(self, distance):
        super().move(distance)
        self.money += distance * self.passengers * 10

    def __str__(self):
        place = super().__str__()
        return "\n".join(
            (
                "Автобус, пассажиров: {0} денег: {1}".format(self.passengers, self.money),
                place
            )
        )

bus = Bus(0, 0, 30)
print(bus)
bus.come_in(10)
bus.move(50)
print(bus)
bus.to_turn(120)
bus.move(100)
print(bus)

