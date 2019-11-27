
# 238. Product of Array Except Self

# https://leetcode.com/problems/product-of-array-except-self/
# https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        temp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] = result[i] * temp
            temp *= nums[i]
        return result
