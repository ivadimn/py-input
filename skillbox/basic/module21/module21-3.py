import random
"""
def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list[:], 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)
print(nums_list)
"""

obj = "string"
print(type(obj))
id1 = id(obj)
obj = obj + "11"
id2 = id(obj)
print("immutable - {0}".format(id1 == id2))