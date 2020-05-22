#Реализация алгоритма колдирования Хаффмана

import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, ac):
        self.left.walk(code, ac + "0")
        self.right.walk(code, ac + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, ac):
        code[self.char] = ac or "0"


def haffman_code(s : str):
    h = []
    for ch, f in Counter(s).items():
        h.append((f, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        f1, _count1, left = heapq.heappop(h)
        f2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (f1 + f2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code



s = input("Введите строку для кодирования : ")
code = haffman_code(s)
coded = "".join(code[ch] for ch in s)
print(f"Исходная строка - {s}")
print("Коды символов:")
for ch in sorted(code):
    print(f"{ch}: {code[ch]}")
print(f"Код - {coded}")