romes = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}


def parse_rome(number: str) -> int:
    result = 0
    prev = 0
    for d in number[::-1]:
        curr = romes.get(d)
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result


num = "XXXIII"
print(parse_rome(num))

