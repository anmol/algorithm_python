#!/usr/bin/env python2.7


# auxiliary procedure
def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = a[p + i]
    for j in range(n2):
        right[j] = a[q + j + 1]
    left[n1] = 1000
    right[n2] = 1000
    i = j = 0
    print p, q, r
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) / 2
        #print q
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
    print a


if __name__ == "__main__":
    a = [5, 3, 9, 2, 4, 1, 3]
    print len(a)
    merge_sort(a, 0, (len(a) - 1))
    #print a
