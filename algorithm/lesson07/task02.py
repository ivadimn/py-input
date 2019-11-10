# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

size = 10
array = [random.random() * 50 for i in range(size)]
print(array)

def sort_merge(a, begin=0, end=-1):
    # Слияние упорядоченных частей массива в буфер temp
    # с дальнейшим переносом содержимого temp в a[b]...a[e]
    def merge(a, b, mid, e):
        # позиция чтения из первой последовательности a[b]...a[mid]
        idx1 = b
        # позиция чтения из второй последовательности a[mid+1]...a[e]
        idx2 = mid + 1
        # текущая позиция записи в temp
        idx3 = 0
        temp = [i for i in range(e - b + 1)]
        # слияние, пока есть хоть один элемент в каждой последовательности
        while idx1 <= mid and idx2 <= e:
            if a[idx1] < a[idx2]:
                temp[idx3] = a[idx1]
                idx1 += 1
                idx3 += 1
            else:
                temp[idx3] = a[idx2]
                idx2 += 1
                idx3 += 1

        # копировать остаток другой в конец буфера
        while idx2 <= e:
            temp[idx3] = a[idx2]
            idx3 += 1
            idx2 += 1
        while idx1 <= mid:
            temp[idx3] = a[idx1]
            idx3 += 1
            idx1 += 1
        a[b:e + 1] = temp
        del (temp)


    if begin < end:  # если есть более 1 элемента
        mid = (begin + end) // 2
        sort_merge(a, begin, mid)
        sort_merge(a, mid + 1, end)
        merge(a, begin, mid, end)

sort_merge(array, 0, len(array) - 1)
print(array)