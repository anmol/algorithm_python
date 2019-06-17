"""
You know the share price of Wooden Orange Toothpicks Inc. (WOT)
will be for the next number of days.
Each day, you can either buy one share of WOT, sell any number
of shares of WOT that you own, or not make any transaction at all.
What is the maximum profit you can obtain with an optimum trading
strategy?

For example, if you know that prices for the next two days are prices = [1, 2],
you should buy one share day one, and sell it day two for a profit of 1.
If they are instead prices = [2, 1], no profit can be made so you don't buy or sell
stock those days.
"""


def stockmax(prices):
    profit = 0
    max_p = 0
    n = len(prices)
    for i in range(n-1, -1, -1):
        if prices[i] >= max_p:
            max_p = prices[i]
        profit += max_p - prices[i]
    return profit


if __name__ == '__main__':
    print stockmax([1, 3, 1, 2])

