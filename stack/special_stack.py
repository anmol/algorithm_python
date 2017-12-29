#!/usr/bin/env python2.7

from stack import Stack
from node import Node


# all operations must be O(1)
class SpecialStack(Stack):

    def __init__(self):
        super(SpecialStack, self).__init__()
        self.min_stack = Stack()

    def push(self, n):
        if super(SpecialStack, self).is_empty():
            print "stack is empty"
            super(SpecialStack, self).push(n)
            self.min_stack.push(Node(n.data))
        else:
            super(SpecialStack, self).push(n)
            last_min = self.min_stack.pop()
            self.min_stack.push(Node(last_min.data))
            if last_min.data > n.data:
                self.min_stack.push(Node(n.data))
            else:
                self.min_stack.push(Node(last_min.data))

    def pop(self):
        item = super(SpecialStack, self).pop()
        self.min_stack.pop()
        return item

    def get_min(self):
        return self.min_stack.head.data


if __name__ == "__main__":
    s = SpecialStack()
    s.push(Node(10))
    s.push(Node(20))
    s.push(Node(40))
    s.push(Node(30))
    s.push(Node(80))
    s.print_stack()
    print s.get_min()
    s.pop()
    s.pop()
    # s.print_stack()
    print s.get_min()



