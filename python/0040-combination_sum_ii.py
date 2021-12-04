
# 40. Combination Sum II

# https://leetcode.com/problems/combination-sum-ii/
# https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(path, target, candidates):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return
            for i in range(len(candidates)):
                # Skip duplicate elements
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtracking(path + [candidates[i]], target - candidates[i], candidates[i + 1:])
        
        result = []
        candidates.sort()
        backtracking([], target, candidates)
        return result
