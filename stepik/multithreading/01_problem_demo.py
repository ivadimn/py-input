import random


def gen_file(filename: str):
    digits = '123456789'
    for i in range(500):
        with open(filename, 'a') as file:
            r = random.random()
            n = ''.join(random.sample(digits, 6))
            if r > 0.5:
                y = f"{n}\n"
                file.write(y)
            else:
                x = f"{int(n) - int(n) * 2}\n"
                file.write(x)


def gen_list() -> list:
    lst = []
    digits = '123456789'
    for i in range(500):
        r = random.random()
        n = ''.join(random.sample(digits, 6))
        if r > 0.5:
            lst.append(n)
        else:
            x = int(n) - int(n) * 2
            lst.append(x)
    return lst


print(gen_list())
