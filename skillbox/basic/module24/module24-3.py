import random

class Toyota:
    color = 'Red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print("Color: {0}\nPrice: {1}\nMax. speed: {2}\nCurrent speed: {3}\n".format(self.color,
                                                     self.price, self.max_speed, self.current_speed))

    def set_current_speed(self, speed):
        self.current_speed = speed
        print("Установлена скорость {0} км/ч.\n".format(self.current_speed))



class Family:
    surname = "Common Family"
    money = 100000
    has_house = False

    def info(self):
        print("Family name: {0}\nFamily funds: {1}\nHaving a house: {2}\n".format(self.surname,
                                                                                     self.money, self.has_house))

    def buy_house(self, price, discount = 0):
        print("Try to buy a house")
        if (self.money >= price - (price * discount) / 100):
            self.money -= price - (price * discount) / 100
            self.has_house = True
            print("House purchased! Current money: {0}\n".format(self.money))
        else:
            print("Not enough money!")

    def earn_funds(self, amount):
        self.money += amount
        print("Earned {0} money! Current value: {1}\n".format(amount, self.money))


family = Family()
family.info()
family.buy_house(1000000)
if not family.has_house:
    family.earn_funds(800000)
    family.buy_house(1000000, 10)

family.info()

