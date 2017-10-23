
# 367. Valid Perfect Square

# https://leetcode.com/problems/valid-perfect-square/description/
# https://discuss.leetcode.com/topic/49325/a-square-number-is-1-3-5-7-java-code
# 1+3+...+(2n-1) = (2n-1 + 1)n/2 = nn


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # a square number is 1+3+5+7+...,
        base = 1
        while num > 0:
            num -= base
            base += 2
        return num == 0


        # my method
        base = 1
        while num // base >= base:
            if num // base == base and ((num + 0.0) / base) % 1 == 0:
                return True
            base += 1
        return False
