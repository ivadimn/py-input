import random

array = [i for i in range(10)]
random.shuffle(array)
print(array)

def sort_insertion(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
        print(array)

sort_insertion(array)
print(array)
