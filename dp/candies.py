"""
Alice is a kindergarten teacher. She wants to give some candies to the
children in her class.  All the children sit in a line and each of them
has a rating score according to his or her performance in the class.
Alice wants to give at least 1 candy to each child. If two children sit
next to each other, then the one with the higher rating must get more candies.
Alice wants to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2].
She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1].
She must buy a minimum of 10 candies.
"""

total = 1
candy = [1]

def restruct(i, arr):
    global total, candy
    if i < 1:
        return
    if arr[i-1] > arr[i] and candy[i-1] <= candy[i]:
        candy[i-1] += 1
        # print candy
        total += 1
        restruct(i-1, arr)

def candies2(n, arr):
    global total, candy
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            while candy[i] <= candy[i-1]:
                candy[i] += 1
                total += 1
            # print candy

        else:
            restruct(i, arr)
    return total

def candies(n, arr):
    global total, candy
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            total += candy[-1] + 1
            candy.append(candy[-1] + 1)
            # print candy
        else:
            candy.append(1)
            total += 1

        #else:
        #    restruct(i, arr)
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and candy[i] <= candy[i+1]:
            incr = candy[i+1] - candy[i] + 1
            candy[i] += incr
            total += incr
    return total

def get_max_from_right(idx, arr):
    # local maxima
    if arr[idx-1] < arr[idx] > arr[idx+1]:
        candy[idx] = max(candy[idx-1], get_max_from_right(idx+1)) + 1
    elif arr[idx+1] < arr[idx]:
        candy[idx] = get_max_from_right(idx+1) + 1
    elif arr[idx-1] < arr[idx]:
        candy[idx] = candy[idx-1] + 1



if __name__ == '__main__':
    # arr = [1, 2, 2]
    arr = [5, 4, 3, 2, 1]
    # arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
    # arr = [9, 2, 3, 6, 5, 4, 3, 2, 2, 2]
    # arr = [5, 4, 3, 2, 1]
    #arr = []
    #total = 0
    # with open('/Users/anmol/Documents/input11.txt') as f:
    #     total = int(f.readline())
    #     for _ in range(total):
    #         arr.append(int(f.readline()))

    # total = len(arr)

    # candy = [1] * total

    print candies(len(arr), arr)

    print arr
    print candy