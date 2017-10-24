
# 400. Nth Digit

# https://leetcode.com/problems/nth-digit/description/
# https://discuss.leetcode.com/topic/59314/java-solution


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find the length of the number where the nth digit is from
        # find the actual number where the nth digit is from
        # find the nth digit and return

        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        start += (n - 1) / length
        return int(str(start)[(n - 1) % length])
