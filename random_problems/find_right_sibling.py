#!/usr/bin/env python2.7

#              o
#             / \
#            /   \
#           o    o
#          / \  / \
#         o  o o  o


class node(object):
    def __init__(self, value):
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.value = value

    def set_parent(self, node):
        self.parent = node

    def set_left(self, node):
        self.leftChild = node
        node.parent = self

    def set_right(self, node):
        self.rightChild = node
        node.parent = self

    def find_right_sibling(self):
        if self.parent == None:
            return None
        elif self.parent.leftChild == self:
            return self.parent.rightChild
        else:
            s = self.parent.find_right_sibling()
            if s is None:
                return None
            elif s.leftChild is not None:
                return s.leftChild
            else:
                return None


if __name__ == "__main__":
    root = node(10)
    print root.value
    root.set_left(node(20))
    root.set_right(node(30))
    root.leftChild.set_left(node(40))
    root.leftChild.set_right(node(50))
    root.rightChild.set_left(node(60))
    root.rightChild.set_right(node(70))
    #n = root.rightChild.rightChild
    n = root.leftChild.rightChild
    print "node : {}".format(n.value)
    r = n.find_right_sibling()
    if r is None:
        print "right sibling : {}".format("None")
    else:
        print "right sibling : {}".format(r.value)



