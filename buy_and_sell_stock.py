"""
BUY AND SELL STOCK

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # slow

        # max = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j]-prices[i] > max:
        #             max = prices[j]-prices[i]
        # return max

        # fast using pointers
        right = 1
        left = 0
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            elif profit < 0:
                left = right
            right+=1
        return max_profit