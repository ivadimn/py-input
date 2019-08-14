import os


def create_dirs():
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), "{}_{}".format("dir", i))
        os.mkdir(new_dir)


def delete_dirs():
    for i in range(1, 10):
        del_dir = "{}_{}".format("dir", i)
        os.removedirs(del_dir)

#create_dirs()
delete_dirs()