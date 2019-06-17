import os
from collections import OrderedDict


def matching_strings(strings, queries):
    uniq = OrderedDict()
    for i in queries:
        uniq[i] = 0

    for i in range(len(strings)):
        if strings[i] in uniq:
            uniq[strings[i]] += 1
    return uniq


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ip = open('/Users/m153/a_projects/algorithm_python/input/sparse_array1_test1', 'r')
    # ip = open('/Users/m153/a_projects/algorithm_python/input/test_0', 'r')
    strings_count = int(ip.readline())

    strings = []

    for _ in range(strings_count):
        strings_item = ip.readline()
        strings.append(strings_item)

    queries_count = int(ip.readline())

    queries = []

    for _ in range(queries_count):
        queries_item = ip.readline()
        queries.append(queries_item)

    res = matching_strings(strings, queries)

    print('\n'.join(map(str, res.values())))
    print('\n')



