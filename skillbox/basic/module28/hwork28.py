from typing import TextIO, List, Tuple
from abc import ABC, abstractmethod
import math
import os

"""
class File:

    def __init__(self, file_name: str, mode: str) -> None:
        self.__file_name = file_name
        self.__mode = mode

    def __enter__(self) -> TextIO:
        if os.path.exists(self.__file_name):
            self.__file = open(self.__file_name, mode = self.__mode)
        else:
            self.__file = open(self.__file_name, mode="w")
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.__file.close()
        return True


with File("examp.txt", "r") as file:
    file.read()



class MyMath:
    pi = 3.1415926535

    class Circle:

        @classmethod
        def square(cls, radius: int) -> float:
            return MyMath.pi * radius * radius

        @classmethod
        def length(cls, radius: int) -> float:
            return 2 * MyMath.pi * radius

    class Cube:

        @classmethod
        def volume(cls, side: int) -> float:
            return side ** 3

    class Sphere:
        @classmethod
        def square(cls, radius: int) -> float:
            return 4 * MyMath.pi * radius * radius



print(MyMath.Circle.length(5))
print(MyMath.Circle.square(5))
print(MyMath.Cube.volume(10))
print(MyMath.Sphere.square(5))


class Figure(ABC):

    @abstractmethod
    def square(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Figure):

    def __init__(self, side: int) -> None:
        self.side = side

    @property
    def side(self) -> int:
        return self._side

    @side.setter
    def side(self, side) -> None:
        self._side = side

    def square(self) -> float:
        return self._side ** 2

    def perimeter(self) -> float:
        return self._side * 4

    def __copy__(self):
        return Square(self.side)

    def __mul__(self, other: int) -> List['Square']:
        lst = []
        for _ in range(other):
            lst.append(self.__copy__())
        return lst

class Triangle(Figure):

    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height
        self.side = math.sqrt((self._base / 2) ** 2 + self._height ** 2)

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, base) -> None:
        self._base = base

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height) -> None:
        self._height = height

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, side: float) -> None:
        self._side = side

    def square(self) -> float:
        return (self._base * self._height) / 2

    def perimeter(self) -> float:
        return self._base + self._side * 2

    def __copy__(self):
        return Triangle(self.base, self.height)

    def __mul__(self, other: int) -> List['Triangle']:
        lst = []
        for _ in range(other):
            lst.append(self.__copy__())
        return lst


class Cube(Figure):

    def __init__(self, side: int) -> None:
        self.__side = side
        self.__figures = Square(side) * 6
        #for _ in range(6):
        #    self.__figures.append(Square(side))

    def square(self) -> float:
        s = 0
        for fg in self.__figures:
            s += fg.square()
        return s

    def perimeter(self) -> float:
        return self.__side * 12


class Pyramid(Figure):

    def __init__(self, base: int, height: int) -> None:
        self.__base = base
        self.__side =  math.sqrt((base / 2) ** 2 + height ** 2)
        self.__figures = [Square(base)]
        self.__figures.extend(Triangle(base, height) * 4)
        #for _ in range(4):
        #    self.__figures.append(Triangle(base, height))

    def square(self) -> float:
        s = 0
        for fg in self.__figures:
            f = fg
            s += f.square()
        return s

    def perimeter(self) -> float:
        return self.__side * 4 + self.__base * 4


cube = Cube(5)
print(cube.square())
print(cube.perimeter())
pyramid = Pyramid(8, 3)
print(pyramid.square())
print(pyramid.perimeter())
"""


class Date:

    def __init__(self):
        self.__day = 0
        self.__month = 0
        self.__year = 0

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        dp = Date.__get_date_parts(date_str)
        if Date.__is_valid(dp):
            dt = Date()
            dt.__day = dp[0]
            dt.__month = dp[1]
            dt.__year = dp[2]
            return dt
        else:
            raise ValueError("Не правильная дата: {0}".format(date_str))

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        date = Date.__get_date_parts(date_str)
        return Date.__is_valid(date)

    @classmethod
    def __get_date_parts(cls, date_str: str) -> Tuple:
        parts = date_str.split("-")
        day, month, year = 0, 0, 0
        if len(parts) != 3:
            return day, month, year
        if parts[0].isdigit():
            day = int(parts[0])
        if parts[1].isdigit():
            month = int(parts[1])
        if parts[2].isdigit():
            year = int(parts[2])

        return day, month, year

    @classmethod
    def __is_valid(cls, date: Tuple) -> bool:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date[1] < 1 or date[1] > 12:
            return False
        if date[0] < 1 or date[0] > days[date[1] - 1]:
            return False
        return True

    def __str__(self):
        return "День: {day}  Месяц: {month}  Год: {year}" \
            .format(day=self.__day, month=self.__month, year=self.__year)


date = Date.from_string('30-11-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))