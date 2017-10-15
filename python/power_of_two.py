
# 231. Power of Two

# https://leetcode.com/problems/power-of-two/description/
# https://discuss.leetcode.com/topic/17857/using-n-n-1-trick


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # bitwise trick
        if n == 0:
            return False
        return True if n & (n - 1) == 0 else False


        # my method
        base = 1
        while base <= n:
            if base == n:
                return True
            base *= 2
        return False
