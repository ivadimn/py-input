# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random, sys

size = 10
array = [random.random() * 50 for i in range(size)]
print(array)


def merge(a, b, mid, e):
    left = a[b:mid+1]
    right = a[mid + 1:e+1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    idx = b
    i = j = 0
    while idx < e:
        if left[i] < right[j]:
            a[idx] = left[i]
            i += 1
        else:
            a[idx] = right[j]
            j += 1
        idx += 1
    del (left)
    del (right)

def sort_merge(a, begin=0, end=-1):

    def merge(a, b, mid, e):
        left = a[b:mid + 1]
        right = a[mid + 1:e + 1]
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        idx = b
        i = j = 0
        while idx < e + 1:
            if left[i] < right[j]:
                a[idx] = left[i]
                i += 1
            else:
                a[idx] = right[j]
                j += 1
            idx += 1


    if begin < end:  # если есть более 1 элемента
        mid = (begin + end) // 2
        sort_merge(a, begin, mid)
        sort_merge(a, mid + 1, end)
        merge(a, begin, mid, end)

sort_merge(array, 0, len(array) - 1)
print(array)