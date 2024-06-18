#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    d = defaultdict(dict)
    for i in range(len(arr)):
        d[arr[i]][i] = 1
        
    for i in range(len(arr)):
        if arr[i] < m:
            m_c = m - arr[i]
            if d.get(m_c, None):
                if d[m_c].get(i, None):
                    del d[m_c][i]
                if d[m_c]:
                    return [i + 1, list(d[m_c].keys())[0] + 1]
            

if __name__ == '__main__':
    fptr = open('./output.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
