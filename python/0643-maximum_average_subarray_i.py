
# 643. Maximum Average Subarray I

# https://leetcode.com/problems/maximum-average-subarray-i/description/


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = window = sum(nums[:k])
        for i in range(k, len(nums)):
            window = window + nums[i] - nums[i - k]
            max_sum = max(window, max_sum)
        return max_sum * 1.0 / k  # for Python 3: max_sum / k
