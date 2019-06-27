import os

rep = {}
tree_edge_list = []
w_sum = 0


def parent(v):
    if rep[v] == v:
        return v
    rep[v] = parent(rep[v])
    return rep[v]


def add_edge(u, v, w):
    global w_sum
    global tree_edge_list
    if u not in rep:
        rep[u] = u
    if v not in rep:
        rep[v] = v
    if parent(u) != parent(v):
        tree_edge_list.append((u, v, w))
        rep[parent(v)] = parent(u)
        w_sum += w


def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    l = sorted(zip(g_from, g_to, g_weight), key=lambda tup: tup[2])
    for i in range(len(l)):
        add_edge(l[i][0], l[i][1], l[i][2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(w_sum))

    fptr.close()
