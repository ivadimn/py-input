import os
import json
#from unittest import mock
my_list = ["aaaa", "bbbbb", "cccc", "ddddd", "eeeeee"]
#print(my_list[3:])

class TimeHelper:
    @staticmethod
    def seconds_hour() -> int:
        return 60 * 60

    @classmethod
    def seconds_day(cls) -> int:
        return cls.seconds_hour() * 24

    @staticmethod
    def count_day(number: int, year: int) -> int:
        count_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = count_days[number]
        if number == 1 and year % 4 == 0:
            count += 1
        return count

    @staticmethod
    def seconds_month(number: int, year: int) -> int:
        return TimeHelper.count_day(number, year) * TimeHelper.seconds_day()


def test_seconds_day():
    th = TimeHelper
    th.seconds_hour = lambda: 1
    assert th.seconds_day() == 24

def test_seconds_month():
    th = TimeHelper
    th.count_day = lambda x, y: 1
    assert th.seconds_month(1, 1) == 24


#print(28 * 3600 * 24)
test_seconds_day()
test_seconds_month()

my_generator = ( i for i in range(10))

print(my_generator.__next__())
print(my_generator.__next__())
print(my_generator.__next__())

