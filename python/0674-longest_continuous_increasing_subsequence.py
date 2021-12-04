
# 674. Longest Continuous Increasing Subsequence

# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        continuous = 1
        max_conti = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continuous += 1
                max_conti = max(max_conti, continuous)
            else:
                continuous = 1
        return max_conti
