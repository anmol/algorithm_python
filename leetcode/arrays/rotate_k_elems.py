#!/usr/bin/env python3


# reverse array subset in place
def rev(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate(nums, k):
    k %= len(nums)
    rev(nums, 0, len(nums) - 1)
    rev(nums, 0, k - 1)
    rev(nums, k, len(nums) - 1)


if __name__ == '__main__':

    a = [1,2,3,4,5,6,7]
    rotate(a, 3)
    print(a)



