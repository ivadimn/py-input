class Beverage:
    all_ingredients = {
        "Strawberries": 1.5,
        "Banana": 0.5,
        "Mango": 2.5,
        "Blueberries": 1.0,
        "Raspberries": 1.0,
        "Apples": 1.75,
        "Pineapple": 3.5
    }

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def get_cost(self) -> str:
        return "${0}".format(self.__calculate())

    def get_price(self) -> str:
        return "${0}".format(self.__calculate() * 2.5)

    def get_name(self) -> str:
        li = []
        for ing in self.ingredients:
            li.append(ing.replace("berries", "berry"))
        li.sort()
        if len(li) > 1:
            li.append("Fusion")
        else:
            li.append("Smoothie")
        return " ".join(li)

    def __calculate(self) -> float:
        cost = 0
        for ing in self.ingredients:
            cost += Beverage.all_ingredients.get(ing)
        return cost

s1 = Beverage(["Banana"])
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Beverage(["Raspberries", "Strawberries", "Blueberries"])
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())