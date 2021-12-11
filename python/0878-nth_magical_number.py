
# 878. Nth Magical Number

# https://leetcode.com/problems/nth-magical-number/
# https://leetcode.com/problems/nth-magical-number/solution/
# https://leetcode.com/problems/nth-magical-number/discuss/1622471/C%2B%2B-Simple-Solution-w-Explanation-or-Brute-Force-%2B-Binary-Search-%2B-Math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        from math import lcm
        MOD = 10 ** 9 + 7

        # Math
        l = lcm(a, b)  # Least common multiple
        m = int(l / a + l / b - 1)  # Number of magic number in one cycle
        q, r = divmod(n, m)

        if r == 0:
            return q * l % MOD

        # Last cycle
        heads = [a, b]
        for _ in range(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += a
            else:
                heads[1] += b
        return (q * l + min(heads)) % MOD


        # Binary search
        l = lcm(a, b)
        left, right = 0, n * min(a, b)
        def magic_below_x(x):
            return (x // a) + (x // b) - (x // l)

        while left < right:
            mid = (left + right) // 2
            if magic_below_x(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left % MOD
