from typing import List
from functools import reduce

"""
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_map = list(map(lambda n: round(n ** 3, 3), floats))
print(floats_map)

names_filter = list(filter(lambda s: len(s) >= 5, names))
print(names_filter)

numbers_reduce = reduce(lambda x, y: x * y, numbers)
print(numbers_reduce)

import timeit


def concat(s1: str, s2: str) -> str:
    result = "-".join([s1, s2])
    return result


res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print( "Время выполнения заданным способом {0}".format(res))

res = timeit.timeit('"-".join(list(map(str, range(100))))', number=10000)
print( "Время выполнения применяя функцию <map()> {0}".format(res))

res = timeit.timeit('import functools\nfunctools.reduce(lambda s1, s2: "-".join([s1, s2]), [str(n) for n in  range(100)])', number=10000)
print( "Время выполнения применяя функцию <reduce()> и lambda {0}".format(res))


strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda e1, e2: {e1: e2}, strings, numbers))
print(result)
"""

def is_prime(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

p = []
for i in range(1001):
    if is_prime(i):
        p.append(i)
print(p)

#pl = [[max for num in range(2, max + 1) if (max % num == 0 and max == num)]  for max in range(2, 1001) if max % 2 != 0]
pl = []
for max in range(2, 1001):
print(pl)