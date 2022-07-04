import pickle

class Store:

    def __init__(self, race, armor, damage = 10):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

    def __str__(self):
        return "Race: {0}, Damage: {1}, Armor: {2}, Health: {2}".format(self.race,
                                                                        self.damage, self.armor, self.health)

    def __repr__(self):
        return "Store('{0}', {1}, {2})".format(self.race, self.armor, self.damage)

    def __setstate__(self, state):
        self.race = state.get("race", "Elf")
        self.damage = state.get("damage", 10)
        self.armor = state.get("armor", 20)
        self.health = state.get("health", 100)



with open("game_state.bin", "rb") as f:
    c1 = pickle.load(f)

print(c1.__dict__)
print(repr(c1))
c2 = eval(repr(c1))
print(c2)