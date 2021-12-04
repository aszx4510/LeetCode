
# 31. Next Permutation

# https://leetcode.com/problems/next-permutation/
# https://leetcode.com/problems/next-permutation/solution/


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp


        def reverse(nums, satrt):
            i, j = satrt, len(nums) - 1
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1


        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            swap(nums, i, j)
        reverse(nums, i + 1)
