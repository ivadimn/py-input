import math
import copy
numbers = [4, 8, 6, 7, 2, 0, -59, -47, -28, -45, 5679, - 3654, 9]


def numbers2(x):
    numbers3 = copy.deepcopy(x)
    number4 = [(round(math.sqrt(number), 2) if number > 0 else number) for number in numbers3]
    return number4


print("old_list = ", numbers)
print("result = ", numbers2(numbers))

