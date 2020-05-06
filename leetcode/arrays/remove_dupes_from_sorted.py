#!/usr/bin/env python3

def remove_duplicates(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != nums[count]:
            nums[count+1] = nums[i]
            count += 1
    return count+1


if __name__ == '__main__':
    print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

