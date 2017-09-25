
# 26. Remove Duplicates from Sorted Array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1  # first element must be inserted 
                nums[i] = nums[j]

        return i + 1
