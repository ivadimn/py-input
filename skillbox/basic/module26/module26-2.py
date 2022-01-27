def iterate(obj):
    iterator = iter(obj)

    while True:
        try:
            elem = iterator.__next__()
            print(elem)
        except:
            break




iterate((1, 0))
f = (10)
a = [1, 2, 3]
b = a.__iter__()
print(b)
d = next(b)
print(d)
e = (1, 0)
h = e.__iter__().__next__()
print(h)

