
# 78. Subsets

# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(indices, n):
            if indices and indices[-1] >= n:
                return []
            result = [[nums[index] for index in indices]]
            start_index = indices[-1] + 1 if indices else 0
            for i in range(start_index, n):
                result += backtracking(indices + [i], n)
            return result
        return backtracking([], len(nums))
