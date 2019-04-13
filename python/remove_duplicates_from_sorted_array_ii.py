
# 80. Remove Duplicates from Sorted Array II

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1
        twice = False
        for fast in range(1, len(nums)):
            if twice and nums[fast] == nums[fast - 1]:
                continue
            if nums[fast] == nums[fast - 1]:
                twice = True
            else:
                twice = False
            nums[slow] = nums[fast]
            slow += 1
        return slow
