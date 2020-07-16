
# 50. Pow(x, n)

# https://leetcode.com/problems/powx-n/
# https://leetcode.com/problems/powx-n/discuss/19546/Short-and-easy-to-understand-solution


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            n *= -1
            x = 1 / x
        return self.myPow(x * x, n // 2) if (n % 2 == 0) else x * self.myPow(x * x, n // 2)

        # concise version
        # if n < 0:
        #     x, n = 1.0/x, -n
        # return int(not n) or [1, x][n%2] * self.myPow(x*x, n//2)
