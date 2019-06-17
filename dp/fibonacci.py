"""
Created on Jul 17, 2018

@author: agautam1
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def memoized_fib(n):
    r = []
    r.append(0)
    r.append(1)
    for i in range(2, n+1):
        r.append(0)
    for j in range(2, n+1):
        r[j] = r[j-1] + r[j-2]
    return r[n]  


if __name__ == '__main__':
    
    print fib(10)
    print memoized_fib(10)