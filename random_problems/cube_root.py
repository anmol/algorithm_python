'''
Created on Jun 22, 2018

@author: agautam1
'''

def calculate_diff(n, mid_cube):
    if n > mid_cube:
        return n - mid_cube
    else:
        return mid_cube - n 
    
def cube_root(n, e):
    start = 0
    end = n
    while(True):        
        mid = (start + end) / 2.0
        mid_cube = mid * mid * mid
        if calculate_diff(n, mid_cube) <= e:
            return mid
        elif mid_cube > n:
            end = mid
        else:
            start = mid

if __name__ == '__main__':
    
    print cube_root(65, 0.00001)