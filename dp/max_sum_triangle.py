'''
Created on Jul 29, 2018

@author: agautam1
'''

def create_triangle(arr):
    arr2 = []
    i = 1
    start = 0
    end = 1
    while len(arr[start:end]) > 0:
        arr2.append(arr[start:end])
        start = end
        i = i + 1
        end = end + i    
    return arr2

def find_max_sum(t_arr):
    s = len(t_arr)
    for i in range(1, s):
        for j in range(len(t_arr[i])):
            if j == 0:
                t_arr[i][j] = t_arr[i][j] + t_arr[i-1][j]
            elif j == len(t_arr[i]) -1:
                t_arr[i][j] = t_arr[i][j] + t_arr[i-1][j-1]
            else:
                t_arr[i][j] = max(t_arr[i-1][j-1], t_arr[i-1][j]) + t_arr[i][j]       
    return max(t_arr[s-1])


if __name__ == '__main__':
    arr = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
    #arr = [3, 7, 4, 2, 4, 6]
    
    t_arr = create_triangle(arr)
    print t_arr
    print find_max_sum(t_arr)
    
    
        
