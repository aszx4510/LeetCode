
# 581. Shortest Unsorted Continuous Subarray

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
# https://discuss.leetcode.com/topic/89282/java-o-n-time-o-1-space


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        beg, end = -1, -2
        min_val, max_val = nums[-1], nums[0]
        for i in range(1, n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n - 1 - i])
            if nums[i] < max_val:
                end = i
            if nums[n - 1 - i] > min_val:
                beg = n - 1 - i
        return end - beg + 1
