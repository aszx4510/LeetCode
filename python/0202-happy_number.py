
# 202. Happy Number

# https://leetcode.com/problems/happy-number/description/
# https://discuss.leetcode.com/topic/12587/my-solution-in-c-o-1-space-and-no-magic-math-property-involved
# Floyd Cycle detection algorithm


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Floyd Cycle detection algorithm
        slow, fast = n, n
        slow = self.digit_square_sum(slow)
        fast = self.digit_square_sum(fast)
        fast = self.digit_square_sum(fast)
        while slow != fast:
            slow = self.digit_square_sum(slow)
            fast = self.digit_square_sum(fast)
            fast = self.digit_square_sum(fast)
        if slow == 1:
            return True
        else:
            return False


    def digit_square_sum(self, n):
        sum = 0
        while n > 0:
            temp = n % 10
            sum += temp * temp
            n = n // 10
        return sum
