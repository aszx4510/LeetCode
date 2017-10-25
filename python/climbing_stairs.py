
# 70. Climbing Stairs

# https://leetcode.com/problems/climbing-stairs/description/
# https://discuss.leetcode.com/topic/19662/python-different-solutions-bottom-up-top-down
# other methods


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        steps = [1, 2, None]
        for i in range(2, n):
            steps[2] = steps[0] + steps[1]
            steps = [steps[1], steps[2], None]
        return steps[1]
