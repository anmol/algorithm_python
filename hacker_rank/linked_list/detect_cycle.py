"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head:
        fast = slow = head
        while True:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            if slow.next:
                slow = slow.next
            else:
                break
            if fast == slow:
                return 1
        return 0
    else:
        return 0
