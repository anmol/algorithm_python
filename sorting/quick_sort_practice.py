#!/usr/bin/env python

#  p  i                          j
# [3, 5, 6, 9, 34, 23, 2, 45, 1, 4]
#  p  i                       j
# [3, 5, 6, 9, 34, 23, 2, 45, 1, 4]
#        i             j
# [3, 1, 6, 9, 34, 23, 2, 45, 5, 4]
#         j  i
# [3, 1, 2, 9, 34, 23, 6, 45, 4, 5]
# -----  o  ----------------------
# [2, 1, 3, 9, 34, 23, 6, 45, 4, 5]

# quick sort is a divide and conquer algorithm


def partition(l, min, max):
    pivot = min
    i = min
    j = max - 1
    while i < j:
        while l[i] <= l[pivot]:
            if i == max - 1:
                break
            i += 1
        while l[j] >= l[pivot]:
            if j == pivot + 1:
                break
            j -= 1
        if i < j:
            l[i],l[j] = l[j],l[i]
    l[pivot], l[j] = l[j], l[pivot]
    return j


def quick_sort(seq, l, u):
    if u - l > 1:
        p = partition(seq, l, u)

        quick_sort(seq, l, p)
        quick_sort(seq, p + 1, u)


if __name__ == "__main__":
    l = [3, 5, 6, 9, 34, 23, 2, 45, 1, 4]
    quick_sort(l, 0, len(l))
    print l
