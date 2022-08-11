class Dot:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) \
               and (self.y == other.y)

    def __lt__(self, other):
        return (self.x <= other.x) or (self.y <= other.y)


def out(dot: Dot, size: int) -> bool:
    return dot.x < 0 or dot.x > size - 1 or dot.y < 0 or dot.y > size - 1