#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    num_str = str(n)
    if len(num_str) == 1:
        return n
    s = 0
    for i in range(len(num_str)):
        s += k * int(num_str[i])
    return superDigit(s, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
