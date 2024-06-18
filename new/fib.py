import os
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        time_taken = t2 - t1
        print(f"time take by {func.__name__}: {time_taken}")
        
        return ret
        
    return wrapper

@time_it
def fib_iter(n: int):
    if n <= 1:
        return n
    fib_2 = 0
    fib_1 = 1
    for _ in range(2, n+1):
        fib = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib
        
    return fib

@time_it
def fib_rec(n: int):
    def _fib_rec(n: int):
        if n <=1:
            return n
        return _fib_rec(n-1) + _fib_rec(n-2)
    return _fib_rec(n)

@time_it
def fib_tail_rec(n: int):
    if n <= 1:
        return n
    def fib_tail_rec(a, b, count):
        if count == 0:
            return b
        return fib_tail_rec(b, a+b, count-1)
    
    return fib_tail_rec(0, 1, n-1)


if __name__ == "__main__":
    # for i in range(10):
    #     print(f"{fib_iter(i)} {fib_rec(i)} {fib_tail_rec(i)}")
    
    print(fib_iter(45))
    print(fib_rec(45))
    print(fib_tail_rec(45))
        