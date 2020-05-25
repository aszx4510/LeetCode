
# 1035. Uncrossed Lines

# https://leetcode.com/problems/uncrossed-lines/
# https://leetcode.com/problems/uncrossed-lines/discuss/282842/JavaC%2B%2BPython-DP-The-Longest-Common-Subsequence
# https://leetcode.com/problems/uncrossed-lines/discuss/651057/Python-by-O(-m*n-)-DP-w-Graph


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # Same as LCS (longest common subsequence)
        m, n = len(A), len(B)
        # 2D-array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + (A[i - 1] == B[j - 1]), dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
