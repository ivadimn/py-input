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
        f1, f2 = f2, (f1 + f2)
        mod = (f1 + f2)  % m

    return mods[:len(mods) - 1]


def fib_mod(n, m):
   mods = period_pizano1(m)
   return mods[n % len(mods)]


def matrix_mult(m1, m2):
    pm = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                pm[i][j] += m1[i][k] * m2[k][j]
    return pm


M1 = [[1, 1], [1, 0]]
M2 = [[1, 1], [1, 0]]
a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
print([[a11, a12], [a21, a22]])
print(matrix_mult(M1, M2))





m = 100000
n = 1000000000000000000
print(bin(n - 1))
#powers = [int(pow(2, b))
#for (b, d) in enumerate(reversed(bin(n-1)[2:])):
#    print(b, d)
    #if d == '1'
#print(powers)
#print(fib(100) % 7)
#print(fib(n))
#print(period_pizano1(m))
print(fib_mod(n, m))

#print(fib_mod(100, 7))