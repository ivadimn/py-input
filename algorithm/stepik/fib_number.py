import cProfile


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

def period_pizano(m):
    mods = [0, 1]
    f1 = 0
    f2 = 1
    fn = f1 + f2
    mod1 = fn % m
    f1, f2 = f2, fn
    fn = f1 + f2
    print(fn, sep=" ")
    mod2 = fn % m
    while not (mod1 == mods[0] and mod2 == mods[1]):
        mods.append(mod1)
        mods.append(mod2)
        f1, f2 = f2, fn
        fn = f1 + f2
        print(fn, sep=" ")
        mod1 = fn % m
        f1, f2 = f2, fn
        fn = f1 + f2
        print(fn, sep=" ")
        mod2 = fn % m
    return mods


def period_pizano1(m):
    mods = [0, 1]
    f1 = 0
    f2 = 1
    fn = f1 + f2
    mod = fn % m
    l = len(mods) - 1
    while not (mods[l] == 0 and mod == 1):
        mods.append(mod)
        l += 1
        f1, f2 = f2, f1 + f2
        mod = (f1 + f2) % m

    return mods[:len(mods) - 1]


def fib_mod(n, m):
   mods = period_pizano1(m)
   return mods[n % len(mods)]

m = 100000
n = 1000000000000000000
print(fib_mod(n, m))

#cProfile.run("fib_mod(n, m)")
