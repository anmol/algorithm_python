#!/usr/bin/env python3
from collections import defaultdict


def time_it(f):
    def wrap(*args, **kwargs):
        from time import time
        st = time()
        ret = f(*args, **kwargs)
        print("time taken by {} is : ".format(f) + str(time() - st))
        return ret
    return wrap


@time_it
def stepPermsRWrap(num):
    def stepPermsR(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        return stepPermsR(n-1) + stepPermsR(n-2) + stepPermsR(n-3)
    return stepPermsR(num)


@time_it
def stepPermsM(num):
    mem = defaultdict(int)

    def stepPermsMemo(n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n] == 0:
            memo[n] = stepPermsMemo(n-1, memo) + stepPermsMemo(n-2, memo) + stepPermsMemo(n-3, memo)
        return memo[n]

    return stepPermsMemo(num, mem)


@time_it
def stepPermsDP(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        paths = [0] * (n+1)
        paths[0] = 1
        paths[1] = 1
        paths[2] = 2
        for i in range(3, n + 1):
            paths[i] = paths[i-1] + paths[i-2] + paths[i-3]
        return paths[n]


if __name__ == '__main__':
    print(stepPermsRWrap(27))
    print(stepPermsM(27))
    print(stepPermsDP(27))

