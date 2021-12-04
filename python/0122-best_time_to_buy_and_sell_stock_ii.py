
# 122. Best Time to Buy and Sell Stock II

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]
        return profit
