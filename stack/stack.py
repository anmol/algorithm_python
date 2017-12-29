#!/usr/bin/env python2.7

from node import Node


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, n):
        if self.count == 0:
            self.head = n
        else:
            temp_head = self.head
            self.head = n
            n.next = temp_head
        self.count += 1

    def pop(self):
        item = self.head
        self.head = self.head.next
        self.count -= 1
        return item

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def print_stack(self):
        print "\nhead:" + str(self.head.data),
        i = self.head
        while i.next is not None:
            print str(i.data) + " ->",
            i = i.next
        print str(i.data)


if __name__ == "__main__":
    s = Stack()
    s.push(Node(10))
    s.push(Node(20))
    s.push(Node(40))
    s.push(Node(30))
    s.push(Node(80))
    s.print_stack()
    s.pop()
    s.pop()
    s.print_stack()

