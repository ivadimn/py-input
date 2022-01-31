import os
from typing import Iterator


def root_path() -> str:
    return os.path.abspath(os.sep)


def gen_files_path(search_folder_name: str, root_dir: str = None) -> Iterator[str]:
    if root_dir is None:
        root_dir = root_path()

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            yield item_path
        if os.path.isdir(item_path):
            folder_name = os.path.basename(item_path)
            if folder_name == search_folder_name:
                print(f'Искомая директория {folder_name} найдена {item_path}')
                raise StopIteration
            for file_path in gen_files_path(search_folder_name, item_path):
                yield file_path

gf = gen_files_path("Lesson05", "/home/vadim/Kotlin")
for file in gf:
    print(file)