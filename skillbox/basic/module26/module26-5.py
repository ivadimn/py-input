"""
def count_generator(count):
    for i in range(count):
        yield i


cg = count_generator(20)
for elem in cg:
    print(elem)

"""

def prime_generator(number):
    prev_value = 2
    for i in range(prev_value, number + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
            prev_value = i + 1
    prev_value += 1


pg = prime_generator(100)
for p in pg:
    print(p, end = " ")