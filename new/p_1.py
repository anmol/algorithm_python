import os

# https://leetcode.com/problems/container-with-most-water/submissions/1288632841/

def max_area(v: list):
    max_area = 0
    l = 0
    r = len(v) - 1
    while l < r:
        max_area = max(max_area, min(v[l], v[r]) * (r - l))
        if v[l] < v[r]:
            l += 1
        else:
            r -= 1
            
    return max_area



if __name__ == "__main__":
    print(max_area([5,9,2,1,4]))
    print(max_area([5,9,2,4,3,7]))