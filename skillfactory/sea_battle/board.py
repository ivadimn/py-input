from typing import List
from dot import Dot


class Board:

    def __init__(self, hidden: bool = False):
        self.__field = [Dot(x, y) for x in range(6) for y in range(6)]
        self.__hidden = hidden
        self.__ships = []

    def __str__(self):
        s_field: List[str] = ["  |{0}|".format("|".join([str(num) for num in range(1, 7)])), "-" * 15]
        for i, s in enumerate(self.__field):
            s_field.append("{0} |{1}|".format(i + 1, "|".join([ch for ch in s])))
        s_field.append("-" * 15)
        return "\n".join(s_field)

