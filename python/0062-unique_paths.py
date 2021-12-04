
# 62. Unique Paths

# https://leetcode.com/problems/unique-paths/


class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                top = dp[i - 1][j] if i != 0 else 0
                left = dp[i][j - 1] if j != 0 else 0
                dp[i][j] = top + left
        return dp[n - 1][m - 1]
