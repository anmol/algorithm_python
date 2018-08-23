#!/usr/bin/env python2.7

from stack import Stack
from node import Node

precedence = {'+': 1,
              '-': 1,
              '*': 2,
              '/': 2,
              '^': 3
              }

s = Stack()


def is_operand(ch):
    return ch.isalpha()


def not_greater(token):
    try:
        if precedence[token] <= precedence[s.head.data]:
            return True
    except KeyError:
        return False


def infix2postfix(expr):
    # initialize stack
    # s.push(Node('('))
    postfix = []
    for token in expr:
        if is_operand(token):
            postfix.append(token)
        elif token == '(':
            s.push(Node(token))
        elif token == ')':
            while not s.is_empty() and s.head.data != '(':
                a = s.pop()
                postfix.append(a.data)
            if not s.is_empty() and s.head.data != '(':
                return -1
            else:
                s.pop()
        else:
            while not s.is_empty() and not_greater(token):
                postfix.append(s.pop().data)
            s.push(Node(token))
    while not s.is_empty():
        postfix.append(s.pop().data)

    print "".join(postfix)


if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    infix2postfix(exp)






