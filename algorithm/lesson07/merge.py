import sys

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




a = [1, 5 ,8 ,10, 15, 2, 7 ,9, 11]
merge(a, 0, 4, 9)