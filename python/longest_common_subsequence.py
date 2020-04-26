
# 1143. Longest Common Subsequence

# https://leetcode.com/problems/longest-common-subsequence/
# https://leetcode.com/problems/longest-common-subsequence/discuss/350993/Python-dp-and-recursive


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if text1[j] == text2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
