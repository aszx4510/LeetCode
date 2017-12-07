
# 724. Find Pivot Index

# https://leetcode.com/problems/find-pivot-index/description/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # copy from submission, change the order
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


        # my version
        left_sum, right_sum = 0, sum(nums)
        for i in range( len(nums)):
            if i != 0:
                left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1
