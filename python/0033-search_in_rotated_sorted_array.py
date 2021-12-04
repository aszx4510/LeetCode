
# 33. Search in Rotated Sorted Array

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the index of smallest value using binary search
        low, high = 0, len(nums) - 1
        while low < high:  # The loop will be stoped when low == high
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # Second binary search
        rotate = low
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            read_mid = (mid + rotate) % len(nums)
            if nums[read_mid] == target:
                return read_mid
            elif nums[read_mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1  # Can't find the result
