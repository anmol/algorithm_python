#!/bin/python3


from collections import (
    defaultdict,
    OrderedDict
)


# Complete the prims function below.
def prims(n, graph, start, S):
    T = OrderedDict()
    S.remove(start)
    T.add(start)
    sum_w = 0
    inf = float('Inf')
    while S:
        u = T.pop()
        T.add(u)
        min_w = inf
        min_v = None
        for v,w in graph[u]:
            if w < min_w:
                min_w = w
                min_v = v
        S.remove(min_v)
        T.add(min_v)
        sum_w += min_w
    return sum_w


if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []
    graph = defaultdict(list)
    S = set()
    T = set()
    for _ in range(m):
        # edges.append(list(map(int, input().rstrip().split())))
        u, v, w = list(map(int, raw_input().rstrip().split()))
        graph[u].append((v, w))
        # graph[v].append((u, w))
        S.add(u)
        S.add(v)

    start = int(raw_input())
    result = prims(n, graph, start, S)
    print result