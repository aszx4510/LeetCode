
# 153. Find Minimum in Rotated Sorted Array

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        # Reference to #33
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
