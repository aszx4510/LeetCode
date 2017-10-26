
# 441. Arranging Coins

# https://leetcode.com/problems/arranging-coins/description/
# https://discuss.leetcode.com/topic/65593/java-clean-code-with-explanations-and-running-time-2-solutions


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # math
        import math
        return int((-1 + math.sqrt(8 * n + 1)) / 2)


        # my method, but O(log(n))
        base = 1
        total = 0
        while total <= n:
            total += base
            base += 1
        return base - 2
