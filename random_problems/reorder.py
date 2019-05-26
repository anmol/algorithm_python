#!/usr/bin/env python

# ptr   i    |                    |
# input  [0, 1, 0, 0, 1, 0, 1, 1, 0]
# output [0, 0, 0, 0, 0, 1, 1, 1, 1]


def reorder(input):
    """

    Args:
        input: List

    Returns: List

    """
    i = 0
    j = len(input) - 1

    while True:
        while input[i] == 0:
            i += 1
        while input[j] == 1:
            j -= 1
        if i > j:
            break
        input[i], input[j] = input[j], input[i]
    return input


if __name__ == '__main__':
    print reorder([0, 1, 0, 0, 1, 0, 1, 1, 0])


