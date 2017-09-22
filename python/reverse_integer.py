
# 7. Reverse Integer

# https://leetcode.com/problems/reverse-integer/description/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) - (x < 0)

        reverse = 0
        x = abs(x)
        while x > 0:
            mod = x % 10
            x = x // 10
            reverse = reverse * 10 + mod

        if reverse > 2147483647 or x < -2147483648:
            return 0

        return reverse * sign
