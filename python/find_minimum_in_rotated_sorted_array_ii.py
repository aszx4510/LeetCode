
# 154. Find Minimum in Rotated Sorted Array II

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:  # nums[mid] == nums[right]
                right -= 1
        return nums[left]
