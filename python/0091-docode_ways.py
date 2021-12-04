
# 91. Decode Ways

# https://leetcode.com/problems/decode-ways/
# https://leetcode.com/problems/decode-ways/discuss/30357/DP-Solution-(Java)-for-reference


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1 if s[n - 1 : n] != '0' else 0

        for i in range(n - 2, -1, -1):
            if s[i:i + 1] == '0':
                continue
            dp[i] += dp[i + 1]
            dp[i] += dp[i + 2] if int(s[i : i + 2]) <= 26 else 0
        return dp[0]
