from board import Board
from dot import Dot
from ship import Ship, Orintation

s = Ship(Dot(1, 0), 3, Orintation.HORIZONTAL)
ship = Ship(Dot(0, 0), length=3)
ship1 = Ship(Dot(1, 3), length=2)
ship2 = Ship(Dot(2, 1), length=2)
ship3 = Ship(Dot(1, 0), length=2)

b = Board()
b.add_ship(ship)
b.add_ship(ship1)
b.add_ship(ship2)
b.add_ship(ship3)

