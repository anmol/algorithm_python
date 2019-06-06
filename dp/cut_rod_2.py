#!/usr/bin/env python

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(l):
    n = len(l)
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, l[i] + cut_rod(l[:n-i]))



