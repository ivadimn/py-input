import random


def newDir2(yourChoise):
    if len(yourChoise) == 0:
        return None
    return random.choice(yourChoise)


testList = ["яблоко", 4, 6.9]
testList2 = []

print(newDir2([1, 2, 3, 4]))
print(newDir2(testList))
print(newDir2(testList2))

