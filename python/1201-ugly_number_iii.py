
# 1201. Ugly Number III

# https://leetcode.com/problems/ugly-number-iii/
# https://leetcode.com/problems/nth-magical-number/solution/
# https://leetcode.com/problems/ugly-number-iii/discuss/387539/cpp-Binary-Search-with-picture-and-Binary-Search-Template


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = ab * c // gcd(ab, c)

        left, right = 0, n * min(a, b, c)
        while left < right:
            mid = (left + right) // 2
            cnt = mid // a + mid // b + mid // c - mid // ab - mid // bc - mid // ac + mid // abc
            if cnt < n:
                left = mid + 1
            else:
                right = mid
        return left
