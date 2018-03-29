
# 747. Largest Number At Least Twice of Others

# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        least = 0
        max_num, max_index = 0, -1
        for i, num in enumerate(nums):
            if num > max_num:
                least = max_num * 2  # second largest
                max_num, max_index = num, i
            else:
                least = max(least, num * 2)
        return max_index if max_num >= least else -1
