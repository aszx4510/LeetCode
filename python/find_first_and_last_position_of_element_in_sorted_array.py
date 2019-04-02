
# 34. Find First and Last Position of Element in Sorted Array

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # Search left-most target
                left_low, left_high = left, mid
                while left_low < left_high:
                    left_mid = (left_low + left_high) // 2
                    if nums[left_mid] == target:
                        left_high = left_mid
                    else:
                        left_low = left_mid + 1
                # Search right-most target
                right_low, right_high = mid, right
                while right_low < right_high:
                    right_mid = math.ceil((right_low + right_high) / 2)
                    if nums[right_mid] == target:
                        right_low = right_mid
                    else:
                        right_high = right_mid - 1
                return [left_high, right_low]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]
