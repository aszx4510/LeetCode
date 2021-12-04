
# 518. Coin Change 2

# https://leetcode.com/problems/coin-change-2/
# https://leetcode.com/problems/coin-change-2/solution/
# https://leetcode.com/problems/coin-change-2/discuss/99210/python-O(n)-space-dp-solution


class Solution(object):
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]
        return dp[-1]

