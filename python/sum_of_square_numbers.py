
# 633. Sum of Square Numbers

# https://leetcode.com/problems/sum-of-square-numbers/description/
# https://discuss.leetcode.com/topic/94435/java-two-pointers-solution


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        if c < 0:
            return False
        left, right = 0, int(sqrt(c))
        while left <= right:
            square_sum = left * left + right * right
            if square_sum < c:
                left += 1
            elif square_sum > c:
                right -= 1
            else:
                return True
        return False
