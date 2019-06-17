"""
calculate the number of pairs having difference k
"""


def pair_diff(arr, k):
    mem = set()
    total = 0
    for i in range(len(arr)):
        if arr[i] - k in mem:
            total += 1
        if arr[i] + k in mem:
            total += 1
        mem.add(arr[i])
    return total


if __name__ == '__main__':
    input = [7, 5, 8, 9, 1]
    print pair_diff(input, 2)