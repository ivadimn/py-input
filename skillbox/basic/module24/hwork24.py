import random
import math

"""
class Warrior:

    def __init__(self, name, health = 100):
        self.name = name
        self.health = 100

    def attack(self, other):
        if not isinstance(other, Warrior):
            return
        if other.health > 0:
            other.health -= 20
        print("\n{0} атаковал {1}".format(self.name, other.name))
        other.print_health()

    def is_live(self):
        return self.health > 0

    def print_health(self):
        if self.is_live():
            print("У {0} осталось {1} здоровья".format(self.name, self.health))
        else:
            print("{0} умер".format(self.name))

warriors = [Warrior("War1"), Warrior("War2")]
count = len(warriors)
while True:
    attack_n = random.randint(0, 1)
    hurt_n = count - attack_n - 1
    warriors[attack_n].attack(warriors[hurt_n])
    if not warriors[hurt_n].is_live():
        print("\n{0} одержал победу!!!".format(warriors[attack_n].name))
        break



class Student:

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def academ_perfomance(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        print("Студент: {0}, Группа №: {1}, Средний балл: {2}".format(self.name, self.group,
                                                                      round(self.academ_perfomance(), 2)))


def read_students():
    sts = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                if line.endswith("\n"):
                    line = line[:-1]
                data = line.split()
                sts.append(Student(" ".join(data[:-1]), data[2], [random.randint(1, 5) for _ in range(5)]))

    except FileNotFoundError:
        print("Файл с данными студентов не найден...")
    return sts

students = read_students()
students_sorted = sorted(students, key=Student.academ_perfomance)
for student in students_sorted:
    student.info()


class Circle:

    def __init__(self, x = 0, y = 0, radius = 1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * (self.radius * self.radius)

    def lenght(self):
        return 2 * math.pi * self.radius

    def increase(self, k):
        self.radius = self.radius * math.sqrt(k)

    def is_intercept(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Parameter <other> has not type Circle")
        delta_x = abs(self.x - abs(other.x))
        delta_y = abs(self.y - other.y)
        return math.sqrt(delta_x ** 2 + delta_y ** 2) <= self.radius + other.radius



c1 = Circle(-4, -4, 4)
c2 = Circle(0, 0, 2)
print(c1.square())
c1.increase(3)
print(c1.square())
print(c1.is_intercept(c2))


class Parent:

    def __init__(self, name, age, childs):
        self.childs = []
        self.name = name
        self.age = age
        for child in  childs:
            if self.age - child.age > 16:
                self.childs.append(child)
            else:
                print("Ребёнок {0} слишком взрослый - {1} лег".format(child.name, child.age))

    def feed(self):
        for child in self.childs:
            if child.state_hunger == 0:
                child.state_hunger = 1
                print("{0} накормлен.".format(child.name))

    def calm_down(self):
        for child in self.childs:
            if child.state_calm == 0:
                child.state_calm = 1
                print("{0} успокоен.".format(child.name))

    def info(self):
        print("\nИмя: {0}\nВозраст: {1}\nДети:".format(self.name, self.age))
        for child in self.childs:
            child.info()




class Child:
    states_calm = {0: "Плачет", 1: "Спокоен"}
    states_hunger = {0: "Голодный", 1: "Сытый"}

    def __init__(self, name, age, state_calm = 0, state_hunger = 0):
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger

    def info(self):
        print("Имя: {0}\nВозраст: {1}\nСостояние спокойствия: {2}\nСостояние голода {3}".format(self.name,
                                                            self.age,
                                                            self.states_calm[self.state_calm],
                                                            self.states_hunger[self.state_hunger]))
        print("-" * 40)

    def cried(self):
        self.state_calm = 0

    def hungry(self):
        self.state_hunger = 0


childs = [Child("Петя", 3), Child("Вова", 6), Child("Аня", 10, 1, 1)]
parent = Parent("Дима", 30, childs)
parent.info()
parent.feed()
parent.calm_down()
parent.info()


class Potato:
    states =  {0: "Неизвестно", 1: "Росток", 2: "Зелёная", 3: "Зрелая", 4: "Собрана"}

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
        self.potatoes = []
        self.sow(count)

    def graw_all(self):
        print("Картошка прорастает!")
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potatoes]):
            print("Картошка ещё не созрела")
            return False
        else:
            print("Картошка уже созрела можно собирать")
            return True

    def give_out(self):
        harvest = []
        if self.are_all_ripe():
            print("Картошка собирана в количестве {0} штук".format(len(self.potatoes)))
            harvest = self.potatoes[:]
            for potato in harvest:
                potato.state = 4
            self.potatoes.clear()
        return harvest

    def sow(self, count):
        if len(self.potatoes) == 0:
            self.potatoes = [Potato(index) for index in range(count)]




class Gardener:

    def __init__(self, name, garden: GardenPotato = None):
        self.name = name
        self.garden = garden
        self.harvest = []

    def set_garden(self, garden: GardenPotato):
        self.garden = garden

    def to_water(self):
        print("Грядка полита!")
        self.garden.graw_all()

    def weed(self):
        print("Грядка прополота!")
        self.garden.graw_all()

    def to_collect(self):
        self.harvest = self.garden.give_out()

    def show_harvest(self):
        print("\nУрожай:")
        for potato in self.harvest:
            potato.print_state()



my_graden = GardenPotato(5)
gardener = Gardener("Jack", my_graden)
gardener.to_water()
gardener.weed()
gardener.to_water()
gardener.to_collect()
gardener.show_harvest()


class Storm:
    answer = "Сложили Воду и Воздух получили Шторм"

class Steam:
    answer = "Сложили Воду и Огонь получили Пар"

class Dirt:
    answer = "Сложили Воду и Землю получили Грязь"

class Lightning:
    answer = "Сложили Воздух и Огонь получили Молнию"

class Dust:
    answer = "Сложили Воздух и Землю получили Пыль"

class Lava:
    answer = "Сложили Огонь и Землю получили Лаву"


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            return None


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Earth:
    def __add__(self, other):
        return None


a = Water()
b = Fire()
c = a + b
print(c.answer)
c = b + a
print(c.answer)
"""

class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

class CardDeck:
    card_suits = ["Пики", "Крести", "Черви", "Буби"]
    card_names = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                  "Валет": 10, "Дама": 10, "Король": 10, "Туз": 11}
    def __init__(self):
        self.card_list = []

    def shuffle(self):
        self.card_list.clear()
        for suit in self.card_suits:
            for name, value in self.card_names.items():
                self.card_list.append(Card(suit, name, value))
        random.shuffle(self.card_list)

    def take_card(self):
        index = random.randint(0, len(self.card_list) - 1)
        card = self.card_list[index]
        self.card_list.pop(index)
        return card

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        score = self.get_score()
        if card.name == "Туз" and score + card.value > 21:
            card.value = 1
        self.cards.append(card)

    def get_score(self):
        score = 0
        for card in self.cards:
            score += card.value
        return score

    def cards_info(self):
        return ", ".join(["{0} {1}".format(card.name, card.suit)  for card in self.cards])

    def show_info(self):
        print("{0} у вас сейчас:".format(self.name))
        print("{0} всего очков {1}".format(self.cards_info(), self.get_score()))


card_deck = CardDeck()
man_hand = Hand("Man")
comp_hand = Hand("Computer")

card_deck.shuffle()
for _ in range(2):
    man_hand.add_card(card_deck.take_card())
    comp_hand.add_card(card_deck.take_card())

while True:
    man_hand.show_info()
    answer = input("\nБудете брать карту? ")
    if answer == "да":
        man_hand.add_card(card_deck.take_card())
        if man_hand.get_score() > 21:
            break
        if comp_hand.get_score() <= 16:
            comp_hand.add_card(card_deck.take_card())
            if comp_hand.get_score() > 21:
                break

    else:
        if comp_hand.get_score() <= 16:
            comp_hand.add_card(card_deck.take_card())
        break
man_score = man_hand.get_score()
comp_score = comp_hand.get_score()

if  man_score <= 21 and man_score > comp_score:
    print("\n{0} выиграл у него {1} ({2})".format(man_hand.name, man_score, man_hand.cards_info()))
    print("У {0} - {1} ({2})".format(comp_hand.name, comp_score, comp_hand.cards_info()))
elif comp_score <= 21 and comp_score > man_score:
    print("\n{0} выиграл у него {1} ({2})".format(comp_hand.name, comp_score, comp_hand.cards_info()))
    print("У {0} - {1} ({2})".format(man_hand.name, man_score, man_hand.cards_info()))
elif man_score > 21:
    print("\n{0} выиграл у него {1} ({2})".format(comp_hand.name, comp_score, comp_hand.cards_info()))
    print("У {0} - {1} перебор! ({2)".format(man_hand.name, man_score, man_hand.cards_info()))
elif comp_score > 21:
    print("\n{0} выиграл у него {1} ({2})".format(man_hand.name, man_score, man_hand.cards_info()))
    print("У {0} - {1} перебор! ({2})".format(comp_hand.name, comp_score, comp_hand.cards_info()))
