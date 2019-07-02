"""
Prims
"""
from collections import defaultdict
import heapq


def initialize(graph, start):
    d = {} # distance dict
    p = {} # parent dict
    pq = [] # 'mutable' priority queue [priority, node, isValid]
    for v in graph:
        p[v] = None
        if v != start:
            d[v] = float('Inf')
        else:
            d[v] = 0
        heapq.heappush(pq, [d[v], v, True])
    return d, p, pq


def relax(u, v, graph, d, p, pq):
    update_pq = True
    if d[v] > graph[u][v]:
        try:
            pq[pq.index([d[v], v, True])][2] = False #make inValid
        except ValueError:
            update_pq = False
        d[v] = graph[u][v]
        p[v] = u
        if update_pq:
            heapq.heappush(pq, [d[v], v, True])


# Complete the prims function below.
def prims(n, graph, start):
    d, p, pq = initialize(graph, start)
    s = set()
    sum_w = 0
    while pq:
        _, u, status = heapq.heappop(pq)
        if not status:
            continue
        s.add(u)
        sum_w += d[u]
        for v in graph[u]:
            if v not in s:
                relax(u, v, graph, d, p, pq)
    return sum_w


if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []
    graph = defaultdict(dict)

    for _ in range(m):
        # edges.append(list(map(int, input().rstrip().split())))
        u, v, w = list(map(int, raw_input().rstrip().split()))
        if u in graph and v in graph[u] and graph[u][v] < w:
            continue
        graph[u][v] = w
        graph[v][u] = w

    start = int(raw_input())
    result = prims(n, graph, start)
    print result