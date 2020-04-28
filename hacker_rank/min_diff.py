#!/usr/bin/python


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    n = len(arr)
    minima = 2 * pow(10, 9)
    for i in range(n):
        for j in range(i):
            if abs(arr[i] - arr[j]) < minima:
                minima = abs(arr[i] - arr[j])
    return minima

if __name__ == '__main__':

