#!/usr/bin/env python2.7

from stack import Stack
from node import Node

s = Stack()


MATRIX = [ [ 0, 0, 0, 0 ],
           [ 0, 0, 1, 0 ],
           [ 0, 0, 0, 0 ],
           [ 0, 0, 1, 0 ] ]


# return True or False based on if a knows b or not
def knows(a, b):
    if MATRIX[a][b] == 1:
        return True
    else:
        return False


def find_celebrity(n):
    for i in range(n):
        s.push(Node(i))
    while s.count > 1:
        a = s.pop()
        b = s.pop()

        if not knows(a.data, b.data) and knows(b.data, a.data):
            s.push(Node(a.data))
        elif not knows(b.data, a.data) and knows(a.data, b.data):
            s.push(Node(b.data))
    if not s.is_empty():
        c = s.pop()
        return c.data
    else:
        return -1


if __name__ == "__main__":
    n = 4
    result = find_celebrity(n)
    if result == -1:
        print "no celebrity"
    else:
        print "celebrity = " + str(result)










