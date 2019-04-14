
# 81. Search in Rotated Sorted Array II

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218/My-8ms-C%2B%2B-solution-(o(logn)-on-average-o(n)-worst-case)


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if (nums[left] == nums[mid]) and (nums[right] == nums[mid]):
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # First half is in order.
                if (nums[left] <= target) and (nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Second half is in order.
                if (nums[mid] < target) and (nums[right] >= target):
                    left = mid + 1
                else:
                    right = mid - 1
        return False
