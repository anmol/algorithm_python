#!/usr/bin/python3


def make_change(coins, money, index, memo):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    amount = 0
    ways = 0
    key = str(money) + "_" + str(index)
    if key in memo.keys():
        return memo[key]
    # print(money, coins[index])
    while amount <= money:
        remaining = money - amount
        ways += make_change(coins, remaining, index+1, memo)
        amount += coins[index]
    memo[key] = ways
    return ways


if __name__ == '__main__':
    print(make_change([10, 5, 1], 20, 0, {}))








