#!/usr/bin/python2.7


def solve(A):
    if A == 0:
        return []
    t = [[1]]
    for i in range(1, A):
        temp = [0] * (i + 1)
        temp[0] = temp[i] = 1
        for j in range(1, i):
            temp[j] = t[i-1][j] + t[i-1][j-1]
        t.append(temp)
    return t

if __name__ == "__main__":
    print solve(0)