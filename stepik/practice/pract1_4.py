from typing import List, Dict
import functools
import sys


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def is_full_house(hand: List[str]):
    if len(hand) != 5:
        return False
    cards = set(hand)
    if len(cards) != 2:
        return False
    else:
        c1 = hand.count(cards.pop())
        c2 = hand.count(cards.pop())
        return (c1 == 2 and c2 == 3) or (c1 == 3 and c2 == 2)


level_sweet = {
    "Plain": 0, "Vanilla": 5, "ChocolateChip": 5, "Strawberry": 10, "Chocolate": 10
}


class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    return max(map(lambda ice: level_sweet[ice.flavor] + ice.sprinkles, lst))


def check_sequence(lst: List[int]) -> int:
   if lst == sorted(set(lst)):
       return 1
   elif lst == sorted(set(lst), reverse=True):
       return -1
   else:
       return 0



def check_sequence1(lst: List[int]) -> int:
    if len(lst) != len(set(lst)):
        return 0
    slst = sorted(lst)
    if all(map(lambda e1, e2: e1 == e2, slst, lst)):
        return 1
    slst = sorted(lst, reverse=True)
    if all(map(lambda e1, e2: e1 == e2, slst, lst)):
        return -1
    return 0


print(check_sequence1([1, 2, 3]))
print(check_sequence1([3, 2, 1]))
print(check_sequence1([1, 2, 1]))
print(check_sequence1([1, 1, 2]))

