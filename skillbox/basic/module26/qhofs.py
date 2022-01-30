from collections.abc import Iterable


def q_hofstadter(seq: list, count: int) -> Iterable:
    if seq[0] != 1 or seq[1] != 1:
        return
    position = 0
    while position < count:
        if position < 2:
            yield 1
        else:
            i1 = position - seq[position - 1]
            i2 = position - seq[position - 2]
            s_n = seq[i1] + seq[i2]
            seq.append(s_n)
            yield s_n
        position += 1



qg = q_hofstadter([1, 1], 25)
for i in qg:
    print(i, end = " ")