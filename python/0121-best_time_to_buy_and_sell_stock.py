
# 121. Best Time to Buy and Sell Stock

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://discuss.leetcode.com/topic/19853/kadane-s-algorithm-since-no-one-has-mentioned-about-this-so-far-in-case-if-interviewer-twists-the-input


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # My new method
        max_profit, min_cost = 0, prices[0]
        for p in prices[1:]:
            max_profit = max(p - min_cost, max_profit)
            min_cost = min(p, min_cost)
        return max_profit


        max_current, profit = 0, 0
        for i in range(1, len(prices)):
            # record the difference between each element
            max_current = max(0, max_current + (prices[i] - prices[i - 1]))
            profit = max(profit, max_current)
        return profit
