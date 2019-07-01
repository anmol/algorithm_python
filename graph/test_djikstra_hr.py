"""
This is specific to the HackerRank problem:
https://www.hackerrank.com/challenges/dijkstrashortreach/problem

Things to remember:
1. The input can have repeated edges, in that case consider the edge
   with the lowest weight to form the graph
2. If you have used Infinity to calculate the distance dictionary, make sure
   to replace it with -1 in the end for the requirements.
   
"""
import heapq
from collections import defaultdict

# Complete the shortestReach function below.


def initialize(graph, s):
    d = {} # distances of each node
    p = {} # parent of each node
    pq = [] # priority queue with `mutable` items
    for v in graph:
        d[v] = float('Inf')  # Initialized as infinity
        p[v] = None
        if v != s:
            heapq.heappush(pq,[d[v], v, True])
    d[s] = 0
    heapq.heappush(pq, [d[s], s, True])
    return d, p, pq


def relax(u, v, graph, d, p, pq):
    update_pq = True
    # graph[u][v] is the weight of the edge (u, v) initialized
    if d[v] > d[u] + graph[u][v]:
        try:
            pq[pq.index([d[v], v, True])][2] = False  # make existing entry invalid
        except ValueError:
            update_pq = False
        d[v] = d[u] + graph[u][v]
        p[v] = u
        if update_pq:
            heapq.heappush(pq,[d[v], v, True])


def shortestReach(n, graph, source):
    d, p, pq = initialize(graph, source)
    s = set()
    while pq:
        _, u, status = heapq.heappop(pq)
        if not status:
            continue
        s.add(u)
        for v in graph[u]:
            relax(u, v, graph, d, p, pq)
    output = [-1] * n
    for k,v in d.items():
        output[k-1] = v if v != float('Inf') else -1
    output.pop(source-1)
    return output


if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in range(t):
        nm = raw_input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []
        graph = defaultdict(dict)

        for _ in range(m):
            #edges.append(list(map(int, input().rstrip().split())))
            u, v, w = list(map(int, raw_input().rstrip().split()))
            if graph.has_key(u) and graph[u].has_key(v) and graph[u][v] < w:
                continue
            graph[u][v] = w
            graph[v][u] = w

        s = int(input())

        result = shortestReach(n, graph, s)
        print result
