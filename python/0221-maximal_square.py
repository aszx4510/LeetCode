
# 221. Maximal Square

# https://leetcode.com/problems/maximal-square/
# https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        ans = 0
        for i in range(len(matrix)):
            dp.append([])
            for j in range(len(matrix[0])):
                dp[i].append(0)
                if matrix[i][j] == '1' and i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i -1][j - 1]) + 1
                elif matrix[i][j] == '1':
                    dp[i][j] = 1
                ans = max(ans, dp[i][j] * dp[i][j])
        return ans
