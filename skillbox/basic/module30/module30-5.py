"""
nums = sorted(list(map(int, input("Введите числа: ").split())))
print(nums)


s = "QQwERtjhdjd111wwww112ccc"

#line = input("Введите строку: ")
linef = list(filter(lambda ch: ch.islower(), s))
print(linef)
"""
from functools import reduce

sentences = ["Nory was a Catholic",
             "because her mother was a Catholic",
             "and Nory’s mother was a Catholic",
             "because her father was a Catholic",
             "and her father was a Catholic",
             "because his mother was a Catholic",
             "or had been"]


def count_was(l1: str, l2: str) -> str:
    result = "".join([l1, l2])
    print(result)
    return result


c = reduce(count_was, sentences).count(" was ")
print(c)