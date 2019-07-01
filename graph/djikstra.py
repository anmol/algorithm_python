"""
Graph: Implemented using a dict which contains vertices V as
       keys whose values are dictionary of vertices(with weights as
       values) reachable from V
"""

import heapq


def initialize(graph, source):
    # shortest path estimate of each v
    d = {}
    # predecessor of each v
    p = {}
    # Priority Queue of 'mutable' items
    pq = []
    for v in graph:
        d[v] = float('Inf')  # Initialized as infinity
        p[v] = None
        if v != source:
            heapq.heappush(pq,[d[v], v, True])
    d[source] = 0
    heapq.heappush(pq, [d[source], source, True])
    return d, p, pq


def relax(u, v, graph, d, p, pq):
    update_pq = True
    if d[v] > d[u] + graph[u][v]:  # graph[u][v] is the weight of the edge (u, v) initialized
        try:
            pq[pq.index([d[v], v, True])][2] = False  # make existing entry invalid
        except ValueError as e:
            update_pq = False
        d[v] = d[u] + graph[u][v]
        p[v] = u
        if update_pq:
            heapq.heappush(pq,[d[v], v, True])


def djikstra(graph, source):
    d, p, pq = initialize(graph, source)
    s = set()
    while pq:
        _, u, status = heapq.heappop(pq)
        if not status:
            continue
        s.add(u)
        for v in graph[u]:
            relax(u, v, graph, d, p, pq)
    return d, p


def test():
    graph = {
        's': {'t': 10, 'y': 5},
        't': {'x': 1,'y': 2},
        'y': {'x': 9, 'z': 2, 't': 3},
        'x': {'z': 4},
        'z': {'s': 7, 'x': 6}

    }

    d, p = djikstra(graph, 's')

    assert d == {
        's': 0,
        't': 8,
        'x': 9,
        'y': 5,
        'z': 7
    }

    assert p == {
        's': None,
        't': 'y',
        'x': 't',
        'y': 's',
        'z': 'y'
    }


if __name__ == '__main__':
    test()
