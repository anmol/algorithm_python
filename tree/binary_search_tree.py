#!/usr/bin/env python2.7

from stack.stack import Stack


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.p = None


def inorder_tree_walk(n):
    s = Stack()
    current = n
    done = 0
    while not done:
        if current is not None:
            s.push(current)
            current = current.left
        else:
            if not s.is_empty():
                current = s.pop()
                print current.val,
                current = current.right
            else:
                done = 1


def search_tree(n, k):
    if k == n.val or n is None:
        return n
    elif k > n.val:
        search_tree(n.right, k)
    else:
        search_tree(n.left, k)


def iterative_search_tree(n, k):
    while n is not None and k != n.val:
        if k < n.val:
            n = n.left
        else:
            n = n.right
    return n


def find_minimum(n):
    while n.left is not None:
        n = n.left
    return n


def find_maximum(n):
    while n.right is not None:
        n = n.right
    return n


def find_successor(r, n):
    if n.right is not None:
        return find_minimum(n.right)
    while r is not None:
        if n.val < r.val:
            succ = r
            r = r.left
        elif n.val > r.val:
            r = r.right
        else:
            break
    return succ


def find_predecessor(root, node):
    pass


def insert(root, key):
    node = TreeNode(key)
    if root is None:
        return node
    else:
        x = root
        while x is not None:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        if node.val < y.val:
            y.left = node
        else:
            y.right = node


def transplant(root, u, v):
    if u.p is None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p




def delete_node(root, key):
    """

    Args:
        root: the root node of the tree
        key: the value of the node to be deleted.

    Returns: None

    """

    # Case 1: Node does not have any children, remove simply.

    # Case 2: Node has only one child

    # Case 3: Node has two children

    pass


if __name__ == "__main__":
    # root = TreeNode(6)
    # root.left = TreeNode(5)
    # root.right = TreeNode(7)
    # root.left.left = TreeNode(2)
    # root.left.right = TreeNode(5)
    # root.right.right = TreeNode(8)

    root = TreeNode(6)
    insert(root, 5)
    insert(root, 7)
    insert(root, 2)
    insert(root, 5)
    insert(root, 8)

    inorder_tree_walk(root)
