
# 90. Subsets II

# https://leetcode.com/problems/subsets-ii/
# https://leetcode.com/problems/subsets-ii/discuss/30158/Standard-DFS-Java-Solution


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, path):
            if not nums:
                return [path]
            result = [path]
            visited = set()
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                result += backtracking(nums[i + 1:], path + [nums[i]])
            return result
        nums.sort()
        return backtracking(nums, [])
