#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    num = 0
    total = 0
    i = 0
    while total <= k:
        if prices[i] <= k - total:
            num += 1
            total += prices[i]
            i += 1
        else:
            break
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
