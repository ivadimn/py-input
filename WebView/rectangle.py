class Rect:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.sq = self.square()

    def square(self):
        return self.height * self.width