
# 326. Power of Three

# https://leetcode.com/problems/power-of-three/description/
# https://discuss.leetcode.com/topic/33536/a-summary-of-all-solutions-new-method-included-at-15-30pm-jan-8th


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        import math
        power = math.log10(n) / math.log10(3)
        if power % 1 == 0:
            return True
        return False
