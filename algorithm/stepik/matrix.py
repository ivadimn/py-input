m = 8
n = 13
memo = {}


def get_powers(m: int) -> list:
    p = []
    for b, d in enumerate(reversed(bin(m - 1)[2:])):
        if d == '1':
            p.append(int(pow(2, b)))
    return p


def power(n: int, p: int) -> int:
    if p == 1:
        return n
    if p in memo:
        return memo[p]
    n = power(n, p // 2)
    memo[p] = n * n
    return memo[p]


pws = get_powers(m)
mat = []
for p in pws:
    mat.append(power(n, p))
while len(mat) > 1:
    n1 = mat.pop()
    n2 = mat.pop()
    mat.append(n1 * n2)

print(mat[0])
print(pow(n, m - 1))