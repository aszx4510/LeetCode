
# 39. Combination Sum

# https://leetcode.com/problems/combination-sum/
# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(path, target, candidates, index):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                backtracking(path + [candidates[i]], target - candidates[i], candidates, i)

        result = []
        backtracking([], target, candidates, 0)
        return result


        # My method with lower efficiency
        # def backtracking(candidate_list, list_sum, candidates):
        #     if list_sum > target:
        #         return
        #     elif list_sum == target:
        #         result.append(candidate_list)
        #     else:
        #         for i in range(len(candidates)):
        #             c = candidate_list[:]
        #             c.append(candidates[i])
        #             backtracking(c, list_sum + candidates[i], candidates[i:])
        #     return
        # result = []
        # backtracking([], 0, candidates)
        # return results