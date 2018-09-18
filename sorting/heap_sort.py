#!/usr/bin/env python2.7

class L(list):
    """
    A subclass of list that can accept additional attributes.
    Should be able to be used just like a regular list.

    The problem:
    a = [1, 2, 4, 8]
    a.x = "Hey!" # AttributeError: 'list' object has no attribute 'x'

    The solution:
    a = L(1, 2, 4, 8)
    a.x = "Hey!"
    print a       # [1, 2, 4, 8]
    print a.x     # "Hey!"
    print len(a)  # 4

    You can also do these:
    a = L( 1, 2, 4, 8 , x="Hey!" )                 # [1, 2, 4, 8]
    a = L( 1, 2, 4, 8 )( x="Hey!" )                # [1, 2, 4, 8]
    a = L( [1, 2, 4, 8] , x="Hey!" )               # [1, 2, 4, 8]
    a = L( {1, 2, 4, 8} , x="Hey!" )               # [1, 2, 4, 8]
    a = L( [2 ** b for b in range(4)] , x="Hey!" ) # [1, 2, 4, 8]
    a = L( (2 ** b for b in range(4)) , x="Hey!" ) # [1, 2, 4, 8]
    a = L( 2 ** b for b in range(4) )( x="Hey!" )  # [1, 2, 4, 8]
    a = L( 2 )                                     # [2]
    """

    def __new__(self, *args, **kwargs):
        return super(L, self).__new__(self, args, kwargs)

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)
        self.__dict__.update(kwargs)

    def __call__(self, **kwargs):
        self.__dict__.update(kwargs)
        return self


def parent(i):
    return (i + 1) / 2 - 1


def left(i):
    return 2 * (i + 1) - 1


def right(i):
    return 2 * (i + 1)


def max_heapify(a, i):
    """
    Args:
        a: input array
        i: index into the array

    Returns:
        None
    """

    l = left(i)
    r = right(i)

    if l < a.heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < a.heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    """

    Args:
        a: input heap array

    Returns:
        None

    """
    a.heap_size = len(a)
    for i in range((len(a) / 2) - 1, -1, -1):
        max_heapify(a, i)


def heap_sort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        a.heap_size = a.heap_size - 1
        max_heapify(a, 0)


if __name__ == "__main__":
    l1 = L(5, 13, 2, 25, 7, 17, 20, 8, 4)
    l1.heap_size = len(l1)
    heap_sort(l1)
    print l1
