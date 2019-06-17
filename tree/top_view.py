"""
top view of a BST
"""

from collections import deque
from binary_search_tree import (
    TreeNode,
    insert,
    inorder_tree_walk
)

nq = deque()
tree_map = {}


def topview(root):
    nq.append((root, 0))
    while len(nq):
        tmp_node = nq.popleft()
        if tmp_node[1] not in tree_map.keys():
            tree_map[tmp_node[1]] = tmp_node[0]
        if tmp_node[0].left:
            nq.append((tmp_node[0].left, tmp_node[1] - 1))
        if tmp_node[0].right:
            nq.append((tmp_node[0].right, tmp_node[1] + 1))

    for key in sorted(tree_map.keys()):
        print tree_map[key].val,


if __name__ == '__main__':
    t = TreeNode(37)
    input = '23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19'
    l = list(input.split(' '))
    for i in l:
        # print i
        insert(t, int(i))
    # inorder_tree_walk(t)
    topview(t)
