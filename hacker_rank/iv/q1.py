#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'getDistanceMetrics' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def getDistanceMetrics(arr):
    d = defaultdict(list)
    n = len(arr)
    res = [0] * n
    for i in range(n):
        d[arr[i]].append(i)
    print(d)
    for i in range(n):
        ls = d[arr[i]]
        for j in range(len(ls)):
            res[i] += abs(i - ls[j])
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # arr_count = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(arr_count):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    print(getDistanceMetrics([1, 2, 2, 1, 5, 1]))
    print(getDistanceMetrics([99, 99, 99, 200, 200, 200]))


    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()