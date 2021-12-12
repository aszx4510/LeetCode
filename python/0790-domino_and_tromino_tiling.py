
# 790. Domino and Tromino Tiling

# https://leetcode.com/problems/domino-and-tromino-tiling/
# https://leetcode.com/problems/domino-and-tromino-tiling/solution/
# https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1%2Bdpn-3


class Solution:
    def numTilings(self, n: int) -> int:
        # Dynamic programming bottom-up
        if n < 2:
            return n

        MOD = 10 ** 9 + 7
        full, partial = [0] * (n + 1), [0] * (n + 1)
        full[1], full[2] = 1, 2
        partial[2] = 1

        for i in range(3, n + 1):
            full[i] = (full[i - 1] + full[i - 2] + partial[i - 1] * 2) % MOD
            partial[i] = (partial[i - 1] + full[i - 2]) % MOD
        return full[n]


        # Math with dynamic programming
        if n == 0:
            return 0

        MOD = 10 ** 9 + 7
        dp = [1, 1, 2, 5]
        if n > 3:
            dp = dp + [0] * (n - 3)
        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= MOD
        return dp[n]
