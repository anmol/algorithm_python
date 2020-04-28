#!/usr/bin/env python3


def luck_balance(k, contests):
    n = len(contests)
    total = sum([y[0] for y in contests])
    imp = list(filter((lambda x: x[1] == 1), contests))
    imp.sort(reverse=True)
    penalty = 0
    for i in range(k, len(imp)):
        penalty += imp[i][0]
    return total - (2 * penalty)


if __name__ == '__main__':
    print(luck_balance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
