
# 540. Single Element in a Sorted Array

# https://leetcode.com/problems/single-element-in-a-sorted-array/
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Two element as a pair and check the pairs composed by same element
        # (0, 1), (2, 3), (4, 5) ...
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            # odd xor 1 = odd-1
            # even xor 1 = even+1
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:  # the single number must in the left-half
                high = mid
        return nums[low]
