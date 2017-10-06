
# 172. Factorial Trailing Zeroes

# https://leetcode.com/problems/factorial-trailing-zeroes/description/
# https://discuss.leetcode.com/topic/6516/my-one-line-solutions-in-3-languages


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 5
        answer = 0
        while n // base != 0:
            answer += n // base
            base *= 5
        return answer

        # recursive method
        # return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
