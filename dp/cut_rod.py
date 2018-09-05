'''
Created on Jul 16, 2018

@author: agautam1
'''


# p = price list , n = length of rod
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = []
    for i in range(n + 1):
        r.append(-1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = []
    for i in range(n + 1):
        r.append(0)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 10
    print cut_rod(p, n)
    print memoized_cut_rod(p, n)
    print bottom_up_cut_rod(p, n)
