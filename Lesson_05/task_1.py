import os

def make_nine_dir():
    for i in range(1, 10):
        name_dir = 'dir_{}'.format(i)
        new_path_dyrectory = os.path.join(os.getcwd(), name_dir)
        os.mkdir(new_path_dyrectory)

def delete_empty_dir():
    list_current_dir = os.listdir(os.getcwd())
    for d in list_current_dir:
        if os.path.isdir(d):
            os.rmdir(d)