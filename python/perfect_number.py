
# 507. Perfect Number

# https://leetcode.com/problems/perfect-number/description/
# https://discuss.leetcode.com/topic/84259/simple-java-solution


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        import math
        sum = 1  # 1 must be the divisor
        for dividor in range(2, int(math.sqrt(num)) + 1):
            if num % dividor == 0:
                sum += dividor + num // dividor
        return sum == num
