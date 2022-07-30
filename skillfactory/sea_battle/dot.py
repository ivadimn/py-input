class Dot:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) \
               and (self.y == other.y)

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return super.__hash__(self)
