#!/bin/python3

import math
import os
import random
import re
import sys


def swap(ar, i):
    ar[i], ar[i+1] = ar[i+1], ar[i]


# Complete the minimumBribes function below.
def minimum_bribes(q):
    num_bribe = 0
    for i in range(len(q) - 1):
        if q[i] > q[i + 1]:
            swap(q, i)
            num_bribe += 1
        if i > 0 and q[i-1] > q[i]:
            print("Too chaotic")
            return
    print(num_bribe)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
