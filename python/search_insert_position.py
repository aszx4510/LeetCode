
# 35. Search Insert Position

# https://leetcode.com/problems/search-insert-position/description/


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        # insert to last
        return i + 1
