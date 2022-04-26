
# 1. Two Sum

# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            if nums[i] in remain:
                return [remain[nums[i]], i]
            else:
                remain[target - nums[i]] = i
