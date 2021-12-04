
# 121. Best Time to Buy and Sell Stock

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://discuss.leetcode.com/topic/19853/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_current, profit = 0, 0
        for i in range(1, len(prices)):
            # record the difference between each element
            max_current = max(0, max_current + (prices[i] - prices[i - 1]))
            profit = max(profit, max_current)
        return profit


        # if not prices:
        #     return 0
        # minimum, maximum = prices[0], prices[0]
        # profit = 0
        # for price in prices:
        #     if price < minimum:
        #         minimum = price
        #         maximum = 0
        #     if price > maximum:
        #         maximum = price
        #         profit = maximum - minimum if maximum - minimum > profit else profit
        # return profit
