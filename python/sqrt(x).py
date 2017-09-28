
# 69. Sqrt(x)

# https://leetcode.com/problems/sqrtx/description/


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton
        r = x
        while r ** 2 > x:
            r = (r + x // r) // 2
        return r
