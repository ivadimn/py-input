num = 1600000000000000000
o = 100000

memo = {}


def get_powers(m: int) -> list:
    p = []
    for b, d in enumerate(reversed(bin(m - 1)[2:])):
        if d == '1':
            p.append(int(pow(2, b)))
    return p


def mult_natrix(m1: list, m2: list) -> list:
    pm = [[0, 0], [0, 0]]
    pm[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    pm[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    pm[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    pm[1][1] = m1[1][0] * m2[0][1] + m2[1][1] * m2[1][1]
    return pm


def power(m: int, p: int) -> int:
    if p == 1:
        return m
    if p in memo:
        return memo[p]
    mp = power(m, p // 2)
    memo[p] = mult_natrix(mp, mp)
    return memo[p]


def fibm(n: int):
    mf = [[1, 1],[1, 0]]
    pws = get_powers(num)
    mat = []
    for p in pws:
        mat.append(power(mf, p))
    while len(mat) > 1:
        m1 = mat.pop()
        m2 = mat.pop()
        mm = mult_natrix(m1, m2)
        mat.append(mm)
    return mat[0][0][0]



print()
#print(pow(n, m - 1))