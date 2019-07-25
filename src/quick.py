def quick(arr, i=0, l=-1):
    if l == -1:
        j = len(arr) - 1
    else:
        j = l
    pivot = find_pivot(arr, i, j)
    if pivot == -1:
        return arr
    k = partition(arr, i, j, pivot)
    quick(arr, i, k - 1)
    quick(arr, k, j)
    return arr


def find_pivot(arr, left, right):
    pivot = left
    for i in range(left, right):
        if pivot < arr[i]:
            return i
        elif arr[i] < pivot:
            return pivot
    return -1


def partition(arr, i, j, pivot):
    p = arr[pivot]
    while True:
        while arr[i] < p:
            i += 1
        while arr[j] >= p:
            j -= 1
        if i > j:
            return i
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
