
# 46. Permutations

# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(path, nums):
            if len(nums) <= 0:
                result.append(path)
                return
            for i in range(len(nums)):
                backtracking(path + [nums[i]], nums[:i] + nums[i + 1:])

        result = []
        backtracking([], nums)
        return result
