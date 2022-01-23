import random

class Home:
    fur_coats = 0
    human_foods = 0
    cat_foods = 0
    total_money = 0

    def __init__(self):
        self.__food = 50
        self.__money = 100
        self.__cat_food = 30
        self.__dirt = 0

    def pollute(self, dirt):
        self.__dirt += dirt

    def clean(self, dirt):
        if self.__dirt >= dirt:
            self.__dirt -= dirt
        else:
            self.__dirt = 0

    def get_dirt(self):
        return self.__dirt

    def take_money(self, name, summa):
        if self.__money >= summa:
            self.__money -= summa
        else:
            summa = self.__money
            self.__money = 0
        print("{0} взяла денег {1}, денег осталось: {2}".format(name, summa, self.__money))
        return summa

    def put_money(self, name, summa):
        self.__money += summa
        print("{0} положил денег {1}, денег стало: {2}".format(name, summa, self.__money))

    def get_money(self):
        return self.__money

    def take_food(self, name, weight):
        result = 0
        if self.__food >= weight:
            self.__food -= weight
            result = weight
        elif 0 < self.__food < weight:
            result = self.__food
            self.__food = 0
        print("{0} взял еды {1}, еды осталось: {2}".format(name, result, self.__food))
        return result

    def take_cat_food(self, name, weight):
        result = 0
        if self.__cat_food >= weight:
            self.__cat_food -= weight
            result = weight
        elif 0 < self.__cat_food < weight:
            result = self.__cat_food
            self.__cat_food = 0
        print("{0} взял еды {1}, еды осталось: {2}".format(name, result, self.__cat_food))
        return result

    def put_food(self, name, weight):
        self.__food += weight
        print("{0} купила еды {1}, еды стало: {2}".format(name, weight, self.__food))

    def put_cat_food(self, name, weight):
        self.__cat_food += weight
        print("{0} купила еды для кота {1}, еды стало: {2}".format(name, weight, self.__cat_food))

    def get_food(self):
        return self.__food

class Member:

    def __init__(self, name: str, home: Home):
        self.name = name
        self.home = home
        self.__fullness = 0
        self.change_fullness(30)

    def eat(self):
        pass

    def operate(self):
        pass

    def change_fullness(self, value):
        self.__fullness += value

    def get_fullness(self):
        return self.__fullness

    def get_happyness(self):
        pass


class Human(Member):

    def __init__(self, name: str, home: Home):
        super().__init__(name, home)
        self.__happiness = 100

    def change_happyness(self, value):
        self.__happiness += value

    def get_happyness(self):
        return self.__happiness

    def eat(self):
        weight = self.home.take_food(self.name, 30)
        self.change_fullness(weight)
        print("{0} поел теперь сытость: {1}".format(self.name, self.get_fullness()))
        self.home.human_foods += weight

    def caress(self):
        self.change_happyness(5)
        self.change_fullness(-10)
        print("{0} погладил кота теперь счастья стало: {1}, а сытости осталось: {2}".
              format(self.name, self.get_happyness(), self.get_fullness()))


class Husband(Human):

    def __init__(self, name: str, home: Home):
        super().__init__(name, home)

    def work(self):
        self.change_fullness(-10)
        print("{0} поработал, заработал 150 денег, теперь сытость: {1}".format(self.name, self.get_fullness()))
        self.home.put_money(self.name, 150)
        self.home.total_money += 150

    def play(self):
        self.change_fullness(-10)
        self.change_happyness(20)
        print("{0} поиграл, теперь счастья: {1}, а сытости осталось: {2}".
              format(self.name, self.get_happyness(), self.get_fullness()))

    def operate(self):
        opers = [self.work, self.eat, self.play, self.caress]
        oper = opers[random.randint(0, 3)]
        if self.home.get_money() <= 50:
            self.work()
        if self.get_fullness() <= 10:
            self.eat()
        else:
            oper()

class Wife(Human):

    def __init__(self, name: str, home: Home):
        super().__init__(name, home)

    def buy_food(self):
        money = home.get_money()
        human_food = money // 2
        human_food = home.take_money(self.name, human_food)
        home.put_food(self.name, human_food)
        money = home.get_money()
        cat_food = money // 6
        cat_food = home.take_money(self.name, cat_food)
        home.put_cat_food(self.name, cat_food)

    def buy_fur_coat(self):
        if home.get_money() >= 350:
            money = home.take_money(self.name, 350)
            self.change_happyness(60)
            self.change_fullness(-10)
            print("{0} купила шубу, теперь степень счастья: {1}, а сытости осталось: {2}".
                  format(self.name, self.get_happyness(), self.get_fullness()))
            self.home.fur_coats += 1
        else:
            print("{0} хотела купить шубу, но денег {1} не хватает".
                  format(self.name, home.get_money()))

    def cleaning(self):
        home.clean(100)
        self.change_fullness(-10)
        print("{0} убралась в доме, теперь загрязненность: {1}, а сытости осталось: {2}".
              format(self.name, home.get_dirt(), self.get_fullness()))

    def operate(self):
        opers = [self.buy_food, self.eat, self.buy_fur_coat, self.cleaning, self.caress]
        oper = opers[random.randint(0, 4)]
        if self.home.get_food() <= 30:
            self.buy_food()
        else:
            oper()

class Cat(Member):

    def __init__(self, name: str, home: Home):
        super().__init__(name, home)

    def eat(self):
        weight = self.home.take_cat_food(self.name, 10)
        self.change_fullness(weight * 2)
        print("{0} поел теперь сытость: {1}".format(self.name, self.get_fullness()))
        self.home.cat_foods += weight

    def sleep(self):
        self.change_fullness(-10)
        print("{0} поспал теперь сытость: {1}".format(self.name, self.get_fullness()))

    def tear_wallpaper(self):
        self.change_fullness(-10)
        self.home.pollute(5)
        print("{0} подрал обои теперь сытость: {1} и грязи в доме стало: {2}".format(self.name,
                                                                               self.get_fullness(),
                                                                               self.home.get_dirt()))

    def get_happyness(self):
        return 20

    def operate(self):
        opers = [self.eat, self.sleep, self.tear_wallpaper]
        oper = opers[random.randint(0, 2)]
        if self.get_fullness() <= 10:
            self.eat()
        else:
            oper()


def is_all_happy(family: list):
    return all([True if memeber.get_happyness() >= 10 else False for memeber in family])

def is_all_wellfed(family: list):
    return all([True if memeber.get_fullness() >= 0 else False for memeber in family])

home = Home()
family = [Husband("Mike", home), Wife("Anna", home), Cat("Murzik", home)]
days = 1

while is_all_wellfed(family) and is_all_happy(family):
    print("День: {}".format(days))
    for member in family:
        member.operate()
        if home.get_dirt() > 90 and isinstance(member, Human):
            member.change_happyness(-10)
    home.pollute(5)
    days += 1
    print("-" * 40)
    print()
    if days == 366:
        break
else:
    for member in family:
        if member.get_fullness() < 0:
            print("{0} умер от голода!".format(member.name))
        if member.get_happyness() < 10:
            print("{0} умер от депрессии!".format(member.name))
print("\nЗа время совместной жизни:")
print("Мужем заработано денег: {0}".format(home.total_money))
print("Людьми съедено еды: {0}".format(home.human_foods))
print("Женой куплено шуб: {0}".format(home.fur_coats))
print("Котом съедено еды: {0}".format(home.cat_foods))



