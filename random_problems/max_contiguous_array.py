#!/usr/bin/env python2.7


def max_sub_array(A):
    #m = sum(A)
    m = n = A[0]

    low = high = temp_low = temp_high = 0
    for i in range(1, len(A)):

        if A[i] >= m and m < 0:
            m = A[i]
            n = A[i]
            low = high = temp_low = temp_high = i
        else:
            if A[i] >= n and n < 0:
                n = A[i]
                temp_low = temp_high = i
            else:
                n += A[i]
                temp_high = i

            if n > m:
                m = n
                low = temp_low
                high = temp_high
    return m, low, high


if __name__ == "__main__":

    #A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    A = [-5, -4, -3, -2, -1]



    print max_sub_array(A)
