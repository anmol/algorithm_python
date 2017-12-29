#!/usr/bin/env python2.7

#node object
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#mergeable stack
# last mean last out
class mergeableStack:
    def __init__(self):
        self.last = None
        self.count = 0

    def push(self, n):
        if self.count == 0:
            self.last = n
            self.last.next = n
        else:
            head = self.last.next
            self.last.next = n
            n.next = head
        self.count += 1

    def pop(self):
        item = self.last.next
        self.last.next = item.next
        self.count -= 1
        return item.data

    def merge(self, s):
        head = self.last.next
        self.last.next = s.last.next
        s.last.next = head
        self.last = s.last
        self.count += s.count

    def printStack(self):
        print "\nhead:" + str(self.last.next.data),
        print "last:" + str(self.last.data)
        i = self.count
        node = self.last.next
        while(i > 0):
            print str(node.data),
            if i > 1:
                print "->",
            node = node.next
            i -= 1



if __name__ == "__main__":

    ms = mergeableStack()

    ms.push(Node(10))
    ms.push(Node(20))
    ms.push(Node(40))
    ms.push(Node(30))
    ms.push(Node(80))
    ms.printStack()
    ms.pop()
    ms.pop()
    ms.printStack()

    ms2 = mergeableStack()
    ms2.push(Node(100))
    ms2.push(Node(200))
    ms2.push(Node(400))
    ms2.push(Node(300))
    ms2.printStack()

    ms.merge(ms2)
    ms.printStack()
    ms.pop()
    ms.printStack()





