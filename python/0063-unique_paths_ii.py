
# 63. Unique Paths II

# https://leetcode.com/problems/unique-paths-ii/


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                top = 0 if i == 0 or obstacleGrid[i - 1][j] else dp[i - 1][j]
                left = 0 if j == 0 or obstacleGrid[i][j - 1] else dp[i][j - 1]
                dp[i][j] = top + left
        return dp[n - 1][m - 1]
