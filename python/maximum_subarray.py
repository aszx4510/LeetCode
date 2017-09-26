
# 53. Maximum Subarray

# https://leetcode.com/problems/maximum-subarray/description/


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        temp_sum = 0
        max_sum = nums[0]  # default first element as max_sum
        for num in nums:
            temp_sum = max(temp_sum + num, num)
            max_sum = max(temp_sum, max_sum)
        return max_sum
