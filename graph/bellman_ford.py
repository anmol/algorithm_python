"""
Graph: Implemented using a dict which contains vertices V as
       keys whose values are dictionary of vertices(with weights as
       values) reachable from V
"""


def initialize(graph, source):
    # shortest path estimate of each v
    d = {}
    # predecessor of each v
    p = {}
    for v in graph:
        d[v] = float('Inf') # Initialized as infinity
        p[v] = None
    d[source] = 0
    return d, p

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]: # graph[u][v] is the weight of the edge (u, v) initialized
        d[v] = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for _ in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                return False
    return d, p

def test():
    graph = {
        's': {'t': 6, 'y': 7},
        't': {'x': 5,'y': 8, 'z': -4},
        'y': {'x': -3, 'z': 9},
        'x': {'t': -2},
        'z': {'s': 2, 'x': 7}

    }

    d, p = bellman_ford(graph, 's')

    assert d == {
        's': 0,
        't': 2,
        'x': 4,
        'y': 7,
        'z': -2
    }

    assert p == {
        's': None,
        't': 'x',
        'x': 'y',
        'y': 's',
        'z': 't'
    }


if __name__ == '__main__':
    test()



