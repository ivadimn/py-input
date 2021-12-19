import random
import math
"""
tup1 = tuple([random.randint(0, 5) for _ in range(10)])
tup2 = tuple([random.randint(-5, 0) for _ in range(10)])
tup3 = tup1 + tup2
print(tup3)
print(tup3.count(0))


def get_squares(r : int, h : int):
    side = 2 * math.pi * r * h
    s_full = side + (2 * (math.pi * (r ** 2)))
    return side, s_full

r = int(input("Введите радиус: "))
h = int(input("Введите высоту: "))
s = get_squares(r, h)
side, s_full = s
print(side)
print(s_full)
"""

def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums_list = list(nums)
    nums_list[index] = value
    return tuple(nums_list), value

my_nums = (1, 2, 3, 4, 5)

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums, r_val = change(new_nums)
rand_val += r_val
print(new_nums, rand_val)