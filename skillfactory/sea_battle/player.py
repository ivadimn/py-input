from abc import ABC, abstractmethod
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
    __dots = [[(0, -1), (0, -2)],
              [(-1, 0), (-2, 0)],
              [(0, 1), (0, 2)],
              [(1, 0), (2, 0)]]
    __dirs = {0: [(0, -1), (0, -2)],
              1: [(0, 1), (0, 2)],
              2: [(-1, 0), (-2, 0)],
              3: [(1, 0), (2, 0)]}

    def __init__(self, dot: Dot, size: int):
        self.__start_dot = dot
        self.__size = size
        self.dots = list()
        self.directs = dict()
        self.__create_dots()
        self.__state = None
        self.__result = ShotResult.WOUNDED

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value: ShotResult):
        self.__result = value

    def __create_dots(self):
        for direct, vals in AiResolve.__dirs.items():
            lst = list()
            for d in vals:
                dot = Dot(self.__start_dot.x + d[0], self.__start_dot.y + d[1])
                if not out(dot, self.__size):
                    lst.append(dot)
            if len(lst) > 0:
                self.directs[direct] = lst

    def next_dot(self, next_line: bool) -> tuple:
        if next_line:
            self.dots.pop(0)
        dots = self.dots[0]
        dot = dots.pop(0)
        return dot.x, dot.y

    def next_dir(self, result: ShotResult) -> Dot:
        if self.__state is None:
            key = list(self.directs.keys())[0]
            self.__state = (key, 0, result)
            return self.directs[key][0]
        if result == ShotResult.WOUNDED:
            key = self.__state[0]
            index = self.__state[1]
            if len(self.directs[key]) > index + 1:
                index += 1
                self.__state = (key, index, result)
                return self.directs[key][index]
            else:
                key += 1
                self.__state = (key, 0, result)
                return self.directs[key][0]
        else:
            key = self.__state[0] + 1
            if self.directs.get(key) is not None:
                self.__state = (key, 0, result)
                return self.directs[key][0]






    def gen_dots(self):
        for line in self.dots:
            print("next line")
            for dot in line:
                print("next dot in line")
                if self.__result == ShotResult.WOUNDED:
                    # self.__result = ShotResult.PAST
                    yield dot.x, dot.y
                    print("after yield")
                else:
                    self.__result = ShotResult.WOUNDED
                    print("to next line")
                    break


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
                self.__ai_resolve.result = self.__result
                return self.__ai_resolve.next_dot(True)
        elif self.__result == ShotResult.WOUNDED:
            if self.__ai_resolve is None:
                self.__ai_resolve = AiResolve(self.__shot_dots[-1], self.enemy_board.size)
            return self.__ai_resolve.next_dot(False)

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
                return self.__result
            except ErrorShot as ex:
                print(ex.args[0], "повторите попытку...")

    def __rand_xy(self) -> tuple:
        x = random.randint(0, self.board.size - 1)
        y = random.randint(0, self.board.size - 1)
        return x, y
