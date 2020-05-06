def max_profit(prices):
    profit = 0
    low = prices[0]
    i = 1
    while i < len(prices):
        while i < len(prices) and prices[i] <= prices[i-1]:
            i += 1
        low = prices[i-1]
        while i < len(prices) and prices[i] >= prices[i-1]:
            i += 1
        high = prices[i-1]
        profit += high - low
    return profit


if __name__ == '__main__':
    print(max_profit([1, 7, 2, 3, 6, 7, 6, 7]))
