from typing import List
from enum import IntEnum
from dot import Dot

class Orintation(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 0

class Ship:

    def __init__(self, bow: Dot, length: int, orientation : Orintation = Orintation.HORIZONTAL):
        self.__bow = bow
        self.__length = length
        self.__orientation = orientation
        self.__health = length

    def dots(self) -> List[Dot]:
        lst = list()
        lst.append(self.__bow)
        for i in range(1, self.__length):
            if self.__orientation == Orintation.HORIZONTAL:
                lst.append(Dot(self.__bow.x, self.__bow.y + i))
            else:
                lst.append(Dot(self.__bow.x + 1, self.__bow.y))
        return lst

    def contour(self) -> List[Dot]:
        dots = self.dots()
        cntr = set()
        for dot in dots:
            cntr.add(Dot(dot.x, dot.y - 1))
            cntr.add(Dot(dot.x, dot.y + 1))
            cntr.add(Dot(dot.x + 1, dot.y))
            cntr.add(Dot(dot.x - 1, dot.y))
        return list(cntr)

    @property
    def health(self) -> int:
        return self.__health


