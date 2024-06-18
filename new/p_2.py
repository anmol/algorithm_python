import os

# Req: 
# 1. len(arr) >= 3
# ∃ i : a[0] < a[1] < ...< a[i]
# a[i] > a[i+1] > ... > a[n-1]

def check_greater(a, b):
    return a > b
def check_less(a, b):
    return a < b



def is_mountain(arr: list):
    if len(arr) < 3:
        return False
    
    i = 1
    switch = 0
    check = check_greater
    
    while i < len(arr):
        curr = arr[i]
        prev = arr[i - 1]
        
        if check(curr, prev):
            i += 1
        elif switch > 0:
            return False
        else:
            switch += 1
            check = check_less
            i += 1
    return switch == 1

def is_mountain_2(arr: list):
    i = 1
    while i < len(arr) and arr[i] > arr[i-1]:
        i += 1
        
    if i == 1 or i == len(arr):
        return False
    
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1
    if i != len(arr):
        return False
    return True
    

if __name__ == "__main__":
    print(is_mountain([0,3,2,1]))
    print(is_mountain([1,2,3,4,5,6,7,8,9]))
    print(is_mountain_2([0,3,2,1]))
    print(is_mountain_2([1,2,3,4,5,6,7,8,9]))
