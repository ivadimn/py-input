import os

path = "/home/vadim/py-input"

for dirpath, dirnames, filenames in os.walk(path):
    print(dirpath, dirnames, filenames)