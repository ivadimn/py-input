from dot import Dot, out

dots = [[(0, -1), (0, -2)],
        [(-1, 0), (-2, 0)],
        [(0, 1), (0, 2)],
        [(1, 0), (2, 0)]]
dirs = {0: [(0, -1), (0, -2)],
        1: [(0, 1), (0, 2)],
        2: [(-1, 0), (-2, 0)],
        3: [(1, 0), (2, 0)]}
odots = [(0, -1), (-1, 0), (0, 1), (1, 0), (0, -2), (-2, 0), (0, 2), (2, 0)]

last = list()
last_result = "u"
directs = dict()
ldots = list()
udots = list()


def create_dots(dot: Dot):
    for item in  odots:
        ld = Dot(dot.x + item[0], dot.y + item[1])
        if not out(ld, 6):
            ldots.append(ld)


def find_next_dot(last_dot: Dot, napr: str) -> Dot:
    if napr == "h":
        ds = list(filter(lambda d: d.x == last_dot.x, ldots))
        # min_d = (ds[0], abs(last_dot.y - ds[0].y))
        # for d in ds:
        #     r = last_dot.y - d.y
        #     if r < min_d[1]:
        #         min_d = (d, r)
    else:
        ds = list(filter(lambda d: d.y == last_dot.y, ldots))
    min_d = min(ds)
    ldots.remove(min_d)
    return min_d


def next_ldot() -> Dot:
    if len(udots) == 1:
        dot1 = ldots.pop(0)
    else:
        napr = "h" if udots[0].x == udots[1].x else "v"
        dot1 = find_next_dot(udots[1], napr)
    return dot1


def print_dots():
    print("{0}".format([str(dot) for dot in ldots]))
    print("*" * 20)


sdot = Dot(3, 5)
create_dots(sdot)
udots.append(sdot)
print_dots()
while True:
    dot = next_ldot()
    print(dot)
    result = input("Result: ")
    if result == "w":
        udots.append(dot)
    elif result == "e":
        break

