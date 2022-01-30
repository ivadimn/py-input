import random

"""
class CountIterator:
    __count = 0

    def __iter__(self):
        CountIterator.__count = 0
        return self

    def __next__(self):
        result = CountIterator.__count
        CountIterator.__count += 1
        return result


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
    if i_elem > 1001:
        break


class Randomizer:
    def __init__(self, limit):
        self.__limit = limit
        self.__count = 0
        self.__prev_value = 0

    def __next__(self):
        self.__count += 1
        if self.__count == 1:
            self.__prev_value = random.random()
            return self.__prev_value
        if self.__count <= self.__limit:
            self.__prev_value += random.random()
            return self.__prev_value
        else:
            raise StopIteration

    def __iter__(self):
        self.__count = 0
        self.__prev_value = 0
        return self

r5 = Randomizer(6)
for elem in r5:
    print(elem)
"""


class Primes:
    def __init__(self, number):
        if number < 2:
            raise ValueError("Параметер не может быть меньше 2")
        self.__max_number = number
        self.__prev_value = 2

    def __next__(self):
        for i in range(self.__prev_value, self.__max_number + 1):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                self.__prev_value = i + 1
                return i
            self.__prev_value = i
        if self.__prev_value == self.__max_number:
            raise StopIteration

    def __iter__(self):
        self.__prev_value = 2
        return self


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')


