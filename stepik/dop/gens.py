import random
import itertools

def randoms(min, max, count):
    for i in range(count):
        yield random.randint(min, max)


rand_sequ = randoms(1, 10, 10)

five_taken = list(itertools.islice(rand_sequ, 5))
print(five_taken)