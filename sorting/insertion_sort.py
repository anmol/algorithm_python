'''
Created on Jul 12, 2018

@author: agautam1
'''

def insertion_sort(l):
    for j in range(1,len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] > key:
            l[i+1] = l[i]
            i -= 1
        l[i + 1] = key
    return l

if __name__ == '__main__':
    l1 = [5,3,9,2,4,1,3]
    print insertion_sort(l1)