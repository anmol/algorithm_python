#!/usr/bin/python3


def partition(arr, p, r):
    pivot = arr[p]
    i = p + 1
    j = r
    while i < j:
        while pivot > arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]
    return j


def _qsort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        _qsort(a, p, q - 1)
        _qsort(a, q + 1, r)


def quicksort(arr):
    _qsort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    arr1 = [5, 7, 9, 2, 6, 1, 4]
    quicksort(arr1)
    print(arr1)
