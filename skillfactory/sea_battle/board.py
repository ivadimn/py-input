from typing import List
from dot import Dot
from ship import Ship, Orintation


class Board:

    def __init__(self, hidden: bool = False):
        self.__field = [Dot(x, y) for x in range(6) for y in range(6)]
        self.__hidden = hidden
        self.__ships = []

    def __str__(self):
        pass

    def add_ship(self, ship: Ship) -> None:
        ocupation_dots = ship.dots() + ship.contour()
        if any([dot in ocupation_dots for dot in ship.dots()]):
            raise Exception("Корабль выходит за пределы поля!!")
        self.__ships.append(ship)


    def out(self, dot: Dot) -> bool:
        return not (dot in self.__field)

