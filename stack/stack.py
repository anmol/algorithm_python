#!/usr/bin/env python2.7


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push([1,2,3])
    print s.peek()

