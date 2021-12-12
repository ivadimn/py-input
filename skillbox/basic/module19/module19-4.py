"""
punkt = set(".,;:!?")
line = list("Я! Есть. Грут?! Я, Грут и Есть.")
count_punt = 0
for p in punkt:
    count_punt += line.count(p)
print(count_punt)
print(sum([line.count(p) for p in punkt]))

import random

nums_1 = set([29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1])
nums_2 = set([16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21])
print(nums_1)
print(nums_2)
nums_1.discard(min(nums_1))
nums_2.discard(min(nums_2))
print(nums_1)
print(nums_2)
nums_1.add(random.randint(100, 200))
nums_2.add(random.randint(100, 200))

print(nums_1.union(nums_2))
print(nums_1.intersection(nums_2))
print(nums_2 - nums_1)
"""

line = "ab1n32kz2"
digit = set([ch for ch in line if ch.isdigit()])
print("".join(digit))
