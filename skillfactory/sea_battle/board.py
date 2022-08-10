from typing import List
import random
from dot import Dot, out
from ship import Ship
from errors import ErrorBuildBoard, ErrorAddShip, ErrorOutOfBoard, ErrorShot
from commons import Orientation, Values, ShotResult



class Board:

    def __init__(self, size: int = 6, hidden: bool = False):
        self.__field = [[Values.SPACE for _ in range(size)] for _ in range(size)]
        self.__size = size
        self.__hidden = hidden
        self.__ships = []

    @property
    def field(self):
        return self.__field

    @property
    def size(self):
        return self.__size

    @property
    def hidden(self) -> bool:
        return self.__hidden

    def value(self, x: int, y: int) -> Values:
        return self.__field[x][y]

    def add_ship(self, ship: Ship) -> None:
        busy_dots = []
        for sh in self.__ships:
            busy_dots.extend(sh.gen_dots() + sh.contour())
        if any([dot in busy_dots for dot in ship.dots()]):
            raise ErrorAddShip()
        for dot in ship.dots():
            self.__field[dot.x][dot.y] = Values.SHIP
        print()
        self.__ships.append(ship)

    def __get_ship(self, dot: Dot) -> Ship:
        for ship in self.__ships:
            if dot in ship.gen_dots():
                return ship

    def out(self, dot: Dot) -> bool:
        return out(dot, self.__size)

    def shot(self, dot: Dot) -> ShotResult:
        if self.out(dot):
            raise ErrorOutOfBoard()
        val = self.__field[dot.x][dot.y]
        if val == Values.SPACE:
            self.__field[dot.x][dot.y] = Values.PAST
            return ShotResult.PAST
        elif val == Values.SHIP:
            ship = self.__get_ship(dot)
            ship.hit()
            self.__field[dot.x][dot.y] = Values.DROP
            if ship.is_live:
                return ShotResult.WOUNDED
            else:
                if self.hidden:
                    self.__contour(ship)
                return ShotResult.KILLED
        else:
            raise ErrorShot()

    @property
    def is_live(self) -> bool:
        return any([sh.is_live for sh in self.__ships])

    def __contour(self, ship: Ship) -> None:
        for dot in ship.contour():
            if not self.out(dot):
                self.field[dot.x][dot.y] = Values.CONTOUR


class BoardBuilder:

    def __init__(self):
        self.__size = 6
        self.__hidden = False

    def set_size(self, size: int) -> "BoardBuilder":
        self.__size = size
        return self

    def set_hidden(self, hidden) -> "BoardBuilder":
        self.__hidden = hidden
        return self

    def build(self, ship_lens: List[int]) -> Board:
        while True:
            try:
                board = self.__random_board(ship_lens)
                return board
            except ErrorBuildBoard as e:
                print(e)
                continue

    def __random_board(self, ship_lens: List[int]) -> Board:
        board = Board(self.__size, self.__hidden)
        for l in ship_lens:
            attempts = 0
            while attempts < 5000:
                x = random.randint(0, self.__size - 1)
                y = random.randint(0, self.__size - 1)
                o = Orientation.HORIZONTAL if random.randint(0, 1) == 0 else Orientation.VERTICAL
                sh = Ship(Dot(x, y), l, o)
                if o == Orientation.HORIZONTAL:
                    is_out = (y + l - 1) > (self.__size - 1)
                else:
                    is_out = (x + l - 1) > (self.__size - 1)
                if is_out:
                    #print("Out: {0}".format(sh))
                    attempts += 1
                    continue
                try:
                    board.add_ship(sh)
                    dots = [str(dot) for dot in sh.dots()]
                    print("Добавлен: {0}, dots = {1}".format(sh, dots))
                    break
                except ErrorAddShip as e:
                    #print("Не добавлен: {0} {1}".format(sh, e))
                    attempts += 1
                    continue
            else:
                raise ErrorBuildBoard()
        return board
