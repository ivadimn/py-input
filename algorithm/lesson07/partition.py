


def partition(a, p, r) -> int :
    x = a[r]
    i = p - 1
    j = p
    while j < r:
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        j += 1
        print(a)
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

array = [2, 8, 7, 1, 3, 5, 6, 4]
index = partition(array, 0, len(array) - 1)
print("*" * 30)
print(index, array)

