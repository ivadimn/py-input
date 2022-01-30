from collections.abc import Iterable
from pathlib import Path
import os


def get_count_string(py_file: str) -> int:
    count : int = 0
    with open(py_file, "r") as f:
        for line in f:
            if not line.startswith("#") and line != "\n":
                count += 1
    return count


def get_count_lines(cur_path : str) -> Iterable:
    if not os.path.exists(cur_path):
        return
    py_files = list(map(str, Path(cur_path).glob("*.py")))
    for file_name in py_files:
        path = os.path.join(cur_path, file_name)
        yield file_name, get_count_string(path)


count_str_gen = get_count_lines(".")
total_lines = 0
for name, count in count_str_gen:
    print("{0}: {1} строк".format(name, count))
    total_lines += count

print("Всего строк в питоновских файлах: {0}".format(total_lines))