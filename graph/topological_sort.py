"""Topological Sort"""

def topological_sort(graph):
    visited = set()
    discover = []
    for v in graph:
        dfs_visit(v, visited, discover)
    return discover


def dfs_visit(v, visited, d):
    if v not in visited:
        visited.add(v)
        d.append(v)
        for k in v.keys():
            dfs_visit(k, visited, d)


if __name__ == '__main__':
    pass