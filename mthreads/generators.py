from time import time

def gen(s):
    for i in s:
        yield i

def gen_filename():
    while True:
        pattern = "file-{0}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(t)


for i in range(513, 1024):
    print(i, chr(i))