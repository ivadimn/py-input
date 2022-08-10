from typing import List
from dot import Dot
from commons import Orientation


class Ship:

    def __init__(self, bow: Dot, length: int, orientation: Orientation = Orientation.HORIZONTAL):
        self.__bow = bow
        self.__length = length
        self.__orientation = orientation
        self.__health = length

    def __str__(self):
        return "Ship(x = {0}, y = {1}, length = {2}, {3})".\
            format(self.__bow.x + 1, self.__bow.y + 1, self.__length, self.__orientation)

    def dots(self) -> List[Dot]:
        lst = list()
        lst.append(self.__bow)
        for i in range(1, self.__length):
            if self.__orientation == Orientation.HORIZONTAL:
                lst.append(Dot(self.__bow.x, self.__bow.y + i))
            else:
                lst.append(Dot(self.__bow.x + i, self.__bow.y))
        return lst

    def contour(self) -> List[Dot]:
        if self.__orientation == Orientation.HORIZONTAL:
            return self.__hcontour()
        else:
            return self.__vcontour()

    def __hcontour(self) -> List[Dot]:
        cntr = list()
        for i in range(self.__length):
            cntr.append(Dot(self.__bow.x - 1, self.__bow.y + i))
            cntr.append(Dot(self.__bow.x + 1, self.__bow.y + i))
        for i in range(-1, 2):
            cntr.append(Dot(self.__bow.x + i, self.__bow.y - 1))
            cntr.append(Dot(self.__bow.x + i, self.__bow.y + self.__length))
        return cntr

    def __vcontour(self) -> List[Dot]:
        cntr = list()
        for i in range(self.__length):
            cntr.append(Dot(self.__bow.x + i, self.__bow.y - 1))
            cntr.append(Dot(self.__bow.x + i, self.__bow.y + 1))
        for i in range(-1, 2):
            cntr.append(Dot(self.__bow.x - 1, self.__bow.y + i))
            cntr.append(Dot(self.__bow.x + self.__length, self.__bow.y + i))
        return cntr

    @property
    def is_live(self) -> bool:
        return self.__health > 0

    def hit(self):
        self.__health -= 1

