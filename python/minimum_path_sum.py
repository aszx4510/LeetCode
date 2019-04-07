
# 64. Minimum Path Sum

# https://leetcode.com/problems/minimum-path-sum/
# https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms


class Solution(object):
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Concise version
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


        # My method
        # dp = [[0 for i in range(m)] for j in range(n)]
        # for i in range(len(dp)):
        #     for j in range(len(dp[0])):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[i][j]
        #             continue
        #         top = dp[i - 1][j] if i != 0 else 99999999999
        #         left = dp[i][j - 1] if j != 0 else 99999999999
        #         dp[i][j] = min(top, left) + grid[i][j]
        # return dp[n - 1][m - 1]
