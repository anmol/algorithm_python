"""
You are working at the cash counter at a fun-fair, and you
have different types of coins available to you in infinite quantities.
The value of each coin is already given.
Determine the number of ways of making change for a particular number
of units using the given types of coins.

For example, if you have 4 types of coins, and the value of each type
is given as 8, 3, 1, 2 respectively, you can make change for 3 units
in three ways: {1, 1, 1}, {1, 2}, and {3} ways

"""
# memoization
# Top Down approach

from pprint import pprint as pp

def get_ways(n, c, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if (n, len(c)) in memo.keys():
        return memo[(n, len(c))]
    sum = 0
    for i in range(len(c)):
        target = n - c[i]
        subc = c[i:]
        result = get_ways(target, subc, memo)
        if result > 0:
            sum += result
    memo[(n, len(c))] = sum
    return sum

# bottom up DP
def get_ways_v2(n, c):
    l = len(c)
    ways = [[0 for x in range(n+1)] for y in range(l)]

    for p in range(0,l):
        ways[p][0] = 1

    for p in range(0, n+1, c[0]):
        #print(p)
        ways[0][p] = 1

    pp(ways)

    for i in range(1,l):
        for j in range(1,n+1):
            p=j-c[i]
            if p <0:
                x=0
            else:
                x=ways[i][p]
            y=ways[i-1][j]
            ways[i][j]= x+y
            pp(ways)
    print(long(ways[l-1][n]))

def get_ways_v3(n, c):
    numways = [0] * (n+1) # numways[x] means ways to get sum x
    numways[0] = 1 # ways to get 0 is 1

    for i in range(len(c)):
        for j in range(c[i], n+1):
            numways[j] += numways[j - c[i]]
    return numways[n]




if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    memo = {}

    c = list(map(int, raw_input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    # ways = get_ways(n, c, memo)
    print get_ways_v3(n, c)

    # print ways


