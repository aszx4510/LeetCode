
# 123. Best Time to Buy and Sell Stock III

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Magic
        first_buy, second_buy = float('inf'), float('inf')
        first_profit, total_profit = 0, 0

        # transaction 1: buy_1, sell_1
        # transaction 2: buy_2, sell_2
        # answer is (sell_1 - buy_1) +  (sell_2 - buy_2)
        for x in prices:
            first_buy = min(x, first_buy)  # first_buy = buy_1
            first_profit = max(x - first_buy, first_profit)  # first_profit = sell_1 - buy_1
            second_buy = min(x - first_profit, second_buy)   # second_buy = buy_2 - (sell_1 - buy_1)
            # total_profit = sell_2 - (buy_2 - (sell_1 - buy_1))
            total_profit = max(x - second_buy, total_profit)
        return total_profit


        # Dynamic Programming, but TLE (Time Limit Exceeded)
        # dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
        if not prices:
            return 0
        dp = [[0] * len(prices) for _ in range(3)] # 3 kinds of transaction (0, 1, 2)
        for k in range(1, 3):
            for i in range(len(prices)):
                minimum = prices[0]
                for j in range(1, i):
                    minimum = min(minimum, prices[j] - dp[k - 1][j - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - minimum)
        return dp[-1][-1]
