
# 162. Find Peak Element

# https://leetcode.com/problems/find-peak-element/
# https://leetcode.com/problems/find-peak-element/discuss/50239/Java-solution-and-explanation-using-invariants


class Solution(object):
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return 0

        # Binary search
        # Runtime: 36 ms, faster than 99.72% of Python3 online submissions for Find Peak Element.
        left, right = 0, len(nums) - 1
        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left if (left == len(nums) - 1 or nums[left] > nums[left + 1]) else right

        # My method
        # Runtime: 40 ms, faster than 99.13% of Python3 online submissions for Find Peak Element.
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return i
