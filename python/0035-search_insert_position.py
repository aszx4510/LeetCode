
# 35. Search Insert Position

# https://leetcode.com/problems/search-insert-position/description/


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Binary search, O(logn)
        # According to the description: You may assume no duplicates in the array.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


        # My old method, O(n)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        # insert to last
        return i + 1
