#!/usr/bin/env python2.7
from stack.stack import Stack
from stack.node import Node

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return (not self.left) and (not self.right)

    def insert_left(self, node):
        if isinstance(node, BinaryTree):
            t = node
        else:
            t = BinaryTree(node)

        if self.left is not None:
            t.left = self.left
        self.left = t

    def insert_right(self, node):
        if isinstance(node, BinaryTree):
            t = node
        else:
            t = BinaryTree(node)

        if self.right is not None:
            t.right = self.right
        self.right = t

    def __repr__(self):
        return '{}'.format(self.value)

    def height(self):
        if self is None:
            return -1
        else:
            if self.left is not None:
                left_height = self.left.height()
            else:
                left_height = 0
            if self.right is not None:
                right_height = self.right.height()
            else:
                right_height = 0
            return 1 + max(left_height, right_height)

    def traverse(self):
        current_level = [self]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                current_level = next_level


def dfs_traverse(tree):
    level = 1
    s = Stack()
    s.push(Node([tree, level]))
    while not s.is_empty():
        node = s.pop()
        key = node.data[0]
        level = node.data[1]
        if level == 1:
            print str(key.value)
        else:
            print (level - 2) * "\t" + u'\u2514\u2500\u2500' + " " + str(key.value)
        if key.left is not None:
            s.push(Node([key.left, level + 1]))
        if key.right is not None:
            s.push(Node([key.right, level + 1]))


if __name__ == "__main__":
    t = BinaryTree(7)
    t.insert_left(3)
    t.insert_right(9)
    t.insert_right(10)
    t.insert_right(14)
    t.insert_left(5)
    t.left.insert_right(4)
    t.right.insert_left(22)
    dfs_traverse(t)

    #print "height: " + str(t.height())