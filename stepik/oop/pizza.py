class Pizza:
    order_number = 0

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

p1 = Pizza(['bacon', 'parmesan', 'ham'])   # order 1
p2 = Pizza.garden_feast()                  # order 2
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)
print(p2.order_number)