from time import time

def gen(s):
    for i in s:
        yield i
        print("next")

def gen_filename():
    while True:
        pattern = "file-{0}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(t)


g = gen("vadim")
print(next(g))
print(next(g))
