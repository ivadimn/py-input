def fib(n):
    if n == 0:
        return 0
    fibs = [0] * (n + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    print(fibs)
    return fibs[n]

def fib_digit(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    last0 = 0
    last1 = 1
    for i in range(2, n + 1):
        lastn = (last0 + last1) % 10
        last0, last1 = last1, lastn
    return lastn

def fib_mod(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    last0 = 0
    last1 = 1
    for i in range(2, n + 1):
        lastn = (last0 + last1) % m
        last0, last1 = last1, lastn
    return lastn

print(fib(100) % 7)

print(fib_mod(100, 7))