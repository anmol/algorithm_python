import os
[1,2,3,4]
[0,1,2,3]

def search_occurence(arr: list, l, r, target: int):
    mid = l + (r - l) // 2
    
    if arr[mid] == target:
        return mid
    elif l == r:
        return -1
    else:
        if arr[mid] < target:
            return search_occurence(arr, mid+1, r, target)
        else:
            return search_occurence(arr, l, mid, target)
        
def get_range(arr: list, target: int):
    index = search_occurence(arr, 0, len(arr) - 1, target)
    print(index)
    
    if index == -1:
        return [-1, -1]
    else:
        l = r = index
        while l >= 0 and arr[l] == target:
            l -= 1
        while r < len(arr) and arr[r] == target:
            r += 1
        return [l+1, r-1]
    
    
if __name__ == "__main__":
    print(get_range([5,7,7,8,8,10], 8))
    
        
        