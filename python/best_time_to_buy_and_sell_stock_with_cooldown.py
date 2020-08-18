
# 309. Best Time to Buy and Sell Stock with Cooldown

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        for p in prices:
            pre_sold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, pre_sold)
        return max(reset, sold)
