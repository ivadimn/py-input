import random


class Home:
    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = 0

    def take_money(self, name, summa):
        summa = self.money // 3
        self.money -= summa
        print("{0} взял денег {1}, денег осталось: {2}".format(name, summa, self.money))
        return summa

    def put_money(self, name, summa):
        self.money += summa
        print("{0} положил денег {1}, денег стало: {2}".format(name, summa, self.money))


    def take_food(self, name, weight):
        result = 0
        if self.food >= weight:
            self.food -= weight
            result = weight
        elif 0 < self.food < weight:
            result = self.food
            self.food = 0
        print("{0} взял еды {1}, еды осталось: {2}".format(name, result, self.food))
        return result

    def put_food(self, name, weight):
        self.food += weight
        print("{0} купил еды {1}, еды стало: {2}".format(name, weight, self.food))


class Man:
    def __init__(self, name, home : Home, fullness = 50):
        self.name = name
        self.home = home
        self.fullness = fullness

    def eat(self):
        food_weight = self.home.take_food(self.name, 50 - self.fullness)
        self.fullness += food_weight
        print("{0} поел теперь сытость - {1}".format(self.name, self.fullness))


    def work(self):
        summa = random.randint(1, 100)
        self.fullness -= random.randint(1, 20)
        self.home.put_money(self.name, summa)
        print("{0} поработал, заработал {1} денег, теперь сытость - {2}".format(self.name, summa, self.fullness))


    def play(self):
        self.fullness -= random.randint(1, 20)
        print("{0} поиграл, теперь сытость - {1}".format(self.name, self.fullness))


    def shopping(self):
        summa = self.home.take_money(self.name, random.randint(1, 50))
        food_weight = summa
        self.home.put_food(self.name, food_weight)
        print("{0} сходил в магазин плюс еды {1} минус денег {2}".format(self.name ,food_weight, summa))

    def act(self):
        number = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.home.food < 10:
            self.shopping()
        elif self.home.money < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.play()

home = Home()
man1 = Man("Вася", home)
man2 = Man("Петя", home)

family = [man1, man2]
days = 1
while man1.fullness >= 0 and man2.fullness >= 0 and days <= 365:
    print("{0} день:".format(days))
    man1.act()
    man2.act()
    print("-" * 50)
    days += 1


if man1.fullness < 0:
    print("\n{0} умер!".format(man1.name))
if man2.fullness < 0:
    print("\n{0} умер!".format(man2.name))
