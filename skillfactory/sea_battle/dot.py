class Dot:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) \
               and (self.y == other.y)

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y)
