'''
Created on Aug 1, 2018

@author: agautam1
'''

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        if n > 0:
            bp = prices[0]
            sp = -1
            
            profit = sp -bp
            
            for i in range(1, n):
                if prices[i] < bp:
                    bp = prices[i]
                elif prices[i] > bp:
                    sp = prices[i]
                    new_profit = sp - bp
                    if new_profit > profit:
                        profit = new_profit
            return max(0, profit)
        else:
            return 0

if __name__ == '__main__':
    #prices = [3,3,5,0,0,3,1,4]
    prices = [2,1,2,1,0,1,2]
    print maxProfit(prices)
    