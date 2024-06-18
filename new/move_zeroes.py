import os

# [0,1,0,3,12] -> [1,3,12,0,0]

""" 


"""

def swap(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]

def move_zeroes(arr: list):
    p1 = p2 = 0
    while p2 < len(arr) - 1:
        print(f"p1 = {p1}, p2 = {p2}")
        while arr[p1] != 0 and p1 < len(arr):
            p1 += 1
            
        while (arr[p2] == 0 or p2 < p1) and p2 < len(arr):
            p2 += 1
        
        swap(arr, p1, p2)
        print(arr)
    
    return arr

def move_zeroes_2(arr: list):
    p1 = p2 = 0
    
    while p2 < len(arr):
        if arr[p2] != 0:
            arr[p1] = arr[p2]
            p1 += 1
        p2 += 1
        
    while p1 < len(arr):
        arr[p1] = 0
        p1 += 1
    
    return arr


if __name__ == "__main__":
    print(move_zeroes([0,1,0,3,12]))
    print(move_zeroes_2([0,1,0,3,12]))

