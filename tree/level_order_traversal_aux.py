"""
level order walk using deque
as an auxiliary data structure
"""
from binary_search_tree import (
    TreeNode,
    insert,
    inorder_tree_walk
)
from collections import deque

def level_order_walk(root):
    tmp_q = deque()
    tmp_q.append(root)
    while len(tmp_q):
        tmp = tmp_q.popleft()
        print tmp.val,
        if tmp.left:
            tmp_q.append(tmp.left)
        if tmp.right:
            tmp_q.append(tmp.right)


if __name__ == '__main__':
    t = TreeNode(37)
    input = '23 108 59 86 64 94 14 105 17 111 65'
    l = list(input.split(' '))
    for i in l:
        # print i
        insert(t, int(i))
    level_order_walk(t)
