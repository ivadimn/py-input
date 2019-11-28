import cProfile
n = 1000000000000000000
m = 100000


def period_pisano(n, m):
    p = []
    p.append(0)
    if m == 1:
        return p
    p.append(1)
    if n <= 1:
        return p

    f0 = 0
    f1 = 1
    for __ in range(m * 6):
        f0, f1 = f1, (f0 + f1) % m
        p.append(f1 % m)
        if p[len(p) - 1] == 1 \
                and p[len(p) - 2] == 0:
            break
    return p[:-2]


pisano = cProfile.run("period_pisano(n, m)")
#print(pisano)
print(pisano[n % len(pisano)])