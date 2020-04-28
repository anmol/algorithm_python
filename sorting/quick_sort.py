#!/usr/bin/env python2.7


# Note : in CLRS index starts from 1 to length of the array
#        Since, the python list index starts from 0
#        we keep the args from 0 to last index i.e., (length - 1)
def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        print q
        print a
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)


if __name__ == "__main__":
    u = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(u, 0, 7)
    print u