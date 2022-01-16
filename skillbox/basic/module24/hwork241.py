<<<<<<< HEAD
class Home:
    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = money

        
=======
import random


class Home:
    def __init__(self, food = 50, money = 0):
        self.food = food
        self.money = 0

    def take_money(self, summa):
        summa = self.money // 3
        self.money -= summa
        print("Взяли денег {0}, денег осталось: {1}".format(summa, self.money))
        return summa

    def put_money(self, summa):
        self.money += summa
        print("Положили денег {0}, денег стало: {1}".format(summa, self.money))


    def take_food(self, weight):
        result = 0
        if self.food >= weight:
            self.food -= weight
            result = weight
        elif 0 < self.food < weight:
            result = self.food
            self.food = 0
        print("Взяли еды {0}, еды осталось: {1}".format(result, self.food))
        return result

    def put_food(self, weight):
        self.food += weight
        print("Купили еды {0}, еды стало: {1}".format(weight, self.food))


class Man:
    def __init__(self, name, home : Home, fullness = 50):
        self.name = name
        self.home = home
        self.fullness = fullness

    def eat(self):
        food_weight = self.home.take_food(50 - self.fullness)
        self.fullness += food_weight
        print("{0} поел теперь сытость - {1}".format(self.name, self.fullness))


    def work(self):
        summa = random.randint(1, 100)
        self.fullness -= random.randint(1, 20)
        self.home.put_money(summa)
        print("{0} поработал, заработал {1} денег, теперь сытость - {2}".format(self.name, summa, self.fullness))


    def play(self):
        self.fullness -= random.randint(1, 20)
        print("{0} поиграл, теперь сытость - {1}".format(self.name, self.fullness))


    def shopping(self):
        summa = self.home.take_money(random.randint(1, 50))
        food_weight = summa
        self.home.put_food(food_weight)
        print("{0} сходил в магазин плюс еды {1} минус денег {2}".format(self.name ,food_weight, summa))



home = Home()
man1 = Man("Вася", home)
man2 = Man("Петя", home)

family = [man1, man2]
days = 1
while man1.fullness >= 0 and man2.fullness >= 0 and days <= 365:
    print("{0} день:".format(days))
    player = family[random.randint(0, 1)]
    number = random.randint(1, 6)
    if player.fullness < 20:
        player.eat()
    elif home.food < 10:
        player.shopping()
    elif home.money < 50:
        player.work()
    elif number == 1:
        player.work()
    elif number == 2:
        player.eat()
    else:
        player.play()
    days += 1
    print("-" * 50)
    #input()

if man1.fullness < 0:
    print("\n{0} умер!".format(man1.name))
if man2.fullness < 0:
    print("\n{0} умер!".format(man2.name))
>>>>>>> module 24 finished
