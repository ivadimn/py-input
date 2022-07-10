import itertools as it

def print_iterable(iterable, end = None):
    for x in iterable:
        if end:
            print(x, end = end)
        else:
            print(x)


lst = list(zip(it.count(), ["a", "b", "c", "d"]))
print(lst)

lst = list(map(pow, range(10), it.repeat(2)))
print(lst)

neg_ones = it.cycle([1, -1])
print(list(next(neg_ones) for _ in range(10)))

print(list(it.accumulate([1, 2, 3, 4, 5, 6])))

print(list(it.chain(["a", "b", "c"], [1, 2, 3, 4, 5], [7, 8, [9, 10, 11]])))




