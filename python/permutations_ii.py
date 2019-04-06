
# 47. Permutations II

# https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(path, nums):
            if len(nums) <= 0:
                result.append(path)
                return
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i - 1]:
                    continue
                backtracking(path + [nums[i]], nums[:i] + nums[i + 1:])

        result = []
        nums.sort()
        backtracking([], nums)
        return result
