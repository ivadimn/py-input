import os


def newDir():
    for i in range(1, 10):
        name = os.path.join(os.getcwd(), "dir_{}".format(i))
        os.mkdir(name)


newDir()
print(os.listdir())


def delDir():
    for i in range(1, 10):
        name = os.path.join(os.getcwd(), "dir_{}".format(i))
        os.rmdir(name)


delDir()
print(os.listdir())
