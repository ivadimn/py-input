# to check uncomment the corresponding lines

# block 1: import modulate

import task_1, task_2

#task_1.make_nine_dir()

task_1.delete_empty_dir()

#print(task_2.random_item([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# block 2: import functions

from task_1 import make_nine_dir, delete_empty_dir
from task_2 import random_item

#make_nine_dir()
#delete_empty_dir()

print(random_item([1, 2, 3, 4, 5, 6, 7, 8, 9]))