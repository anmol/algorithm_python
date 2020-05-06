#!/bin/python3

import math
import os
import random
import re
import sys
import re



#
# Complete the 'getPotentialDomains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#

def getPotentialDomains(lines):
    domain_set = set()
    pattern = 'https|http?://(www\.|ww2\.|web\.)*([A-Za-z_0-9.-]+).*'
    for line in lines:
        m = re.search(pattern, line)
        domain_name = m.group(2)
        domain_set.add(domain_name)
    domain_list = sorted(list(domain_set))
    res = ''
    return ';'.join(domain_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lines_count = int(input().strip())

    lines = []

    for _ in range(lines_count):
        lines_item = input()
        lines.append(lines_item)

    result = getPotentialDomains(lines)

    fptr.write(result + '\n')

    fptr.close()
