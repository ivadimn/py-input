from abc import ABC, abstractmethod
from typing import List
from board import Board
from ship import Ship
from errors import ErrorOutOfBoard, ErrorShot
from dot import Dot, out
from commons import ShotResult, Orientation
import random


class Player(ABC):

    def __init__(self, name: str, board: Board, enemy_board: Board):
        self.__name = name
        self.board = board
        self.enemy_board = enemy_board

    @abstractmethod
    def ask(self) -> tuple: ...

    @abstractmethod
    def move(self) -> ShotResult: ...


class User(Player):

    def __init__(self, name: str, board: Board, enemy_board: Board):
        super().__init__(name, board, enemy_board)

    def ask(self) -> tuple:
        while True:
            try:
                vals = list(map(int, input("Ваш ход: ").split()))
                if len(vals) != 2:
                    raise ValueError()
                return vals[0] - 1, vals[1] - 1
            except ValueError:
                print("Ошибка ввода, повторите попытку...")
                continue

    def move(self) -> ShotResult:
        while True:
            x, y = self.ask()
            try:
                result = self.enemy_board.shot(Dot(x, y))
                return result
            except ErrorOutOfBoard as ex:
                print(ex.args[0], "повторите попытку...")
            except ErrorShot as ex:
                print(ex.args[0], "повторите попытку...")


class AiResolve:
    __pos_dots = [(0, -1), (-1, 0), (0, 1), (1, 0), (0, -2), (-2, 0), (0, 2), (2, 0)]

    def __init__(self, sh_dots: List[Dot], size: int):
        self.__luck_dots = list()
        self.__luck_dots.append(sh_dots[-1])
        self.__size = size
        self.dots = list()
        self.__create_dots(sh_dots)

    def append_luck_dot(self, dot: Dot) -> None:
        self.__luck_dots.append(dot)

    def __create_dots(self, sh_dots: List[Dot]):
        dot: Dot = self.__luck_dots[0]
        for item in AiResolve.__pos_dots:
            ld = Dot(dot.x + item[0], dot.y + item[1])
            if not out(ld, self.__size) and (ld not in sh_dots):
                self.dots.append(ld)

    def find_next_dot(self, last_dot: Dot, direct: str) -> Dot:
        if direct == "hor":
            ds = filter(lambda d: d.x == last_dot.x, self.dots)
        else:
            ds = filter(lambda d: d.y == last_dot.y, self.dots)
        min_d = min(ds)
        self.dots.remove(min_d)
        return min_d

    def next_dot(self) -> tuple:
        if len(self.__luck_dots) == 1:
            dot = self.dots.pop(0)
        else:
            direct = "hor" if self.__luck_dots[0].x == self.__luck_dots[1].x else "ver"
            dot = self.find_next_dot(self.__luck_dots[1], direct)
        return dot.x, dot.y


class Ai(Player):

    def __init__(self, name: str, board: Board, enemy_board: Board):
        super().__init__(name, board, enemy_board)
        self.__shot_dots = list()
        self.__result = ShotResult.PAST
        self.__ai_resolve = None
        self.__dots = None

    def ask(self) -> tuple:
        if self.__result == ShotResult.KILLED:
            if self.__ai_resolve:
                self.__ai_resolve = None
            return self.__rand_xy()
        elif self.__result == ShotResult.PAST:
            if self.__ai_resolve is None:
                return self.__rand_xy()
            else:
                return self.__ai_resolve.next_dot()
        elif self.__result == ShotResult.WOUNDED:
            if self.__ai_resolve is None:
                self.__ai_resolve = AiResolve(self.__shot_dots, self.enemy_board.size)
            else:
                self.__ai_resolve.append_luck_dot(self.__shot_dots[-1])

            return self.__ai_resolve.next_dot()

    def move(self) -> ShotResult:
        print("Ход компьютера!")
        while True:
            x, y = self.ask()
            dot = Dot(x, y)
            if dot in self.__shot_dots:
                continue
            try:
                self.__result = self.enemy_board.shot(dot)
                self.__shot_dots.append(dot)
                if self.__result == ShotResult.KILLED:
                    self.__add_contour_dots(dot)
                return self.__result
            except ErrorShot as ex:
                print(ex.args[0], "повторите попытку...")

    def __rand_xy(self) -> tuple:
        x = random.randint(0, self.board.size - 1)
        y = random.randint(0, self.board.size - 1)
        return x, y

    def __add_contour_dots(self, dot: Dot) -> None:
        ship = self.enemy_board.get_ship(dot)
        for d in ship.contour():
            if d not in self.__shot_dots:
                self.__shot_dots.append(d)