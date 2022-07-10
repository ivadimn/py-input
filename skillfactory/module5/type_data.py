M = {'a': 1,
     'b': 0,
     'c': -1}


def D(a, b, c):
    return b ** 2 - 4 * a * c

def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return "Нет вещественных корней"
    elif D(a, b, c) == 0:
        return -b / (2 * a)
    else:
        return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

def min_e(l: list) -> int:
    melem = l.pop(0)
    if len(l) == 1:
        return melem if melem < l[0] else l[0]
    else:
        e = min_e(l)
        return melem if melem < e else e

L = ['THIS', 'IS', 'LOWER', 'STRING']


a = ["это", "маленький", "текст", "обидно"]
print(list(map(str.capitalize, a)))


