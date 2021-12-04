
# 216. Combination Sum III

# https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(path, n, target):
            if target == 0 and n == 0:
                result.append(path)
            elif (target < 0) or (n < 0):
                return
            else:
                for i in range(1, 10):
                    if path and i <= path[-1]:
                        continue
                    backtracking(path[:] + [i], n - 1, target - i)

        result = []
        backtracking([], k, n)
        return result
