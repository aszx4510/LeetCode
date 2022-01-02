
# 902. Numbers At Most N Given Digit Set

# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Dynamic Programming
        s = str(n)
        k = len(s)

        # dp[i] means total number of valid interger with length k if n was "n[i:]"
        dp = [0] * k + [1]

        for i in range(k - 1, -1, -1):
            print(i, int(s[i]))

            for d in digits:
                print
                if d < s[i]:
                    dp[i] += len(digits) ** (k - i - 1)
                if d == s[i]:
                    dp[i] += dp[i + 1]

        return dp[0] + sum(len(digits) ** i for i in range(1, k))
