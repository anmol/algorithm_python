#!/usr/bin/env python3


def move_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    for i in range(count, len(nums)):
        nums[i] = 0
    print(nums)


if __name__ == '__main__':
    move_zeroes([0, 1, 0, 3, 12])
