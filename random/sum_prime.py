'''
Created on Jun 5, 2018

@author: agautam1
'''
#Project Euler problem 10
import sys
import math
import time

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in xrange(2,n):
#         if (n % i) == 0:
#             return False
#     return True
        
def generate_prime(n):
    while(True):
        if is_prime(n):
            yield n
        n += 1
            
        

if __name__ == '__main__':
    start = time.time()
    s = 2
    # 2 + 3 + 5 + 7
    for p in generate_prime(3):
        if p < 2000000:
            s += p
        else:
            print s
            end = time.time()
            print "Time taken in seconds: ", (end - start)
            sys.exit(0)