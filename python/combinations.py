
# 77. Combinations

# https://leetcode.com/problems/combinations/
# https://leetcode.com/problems/combinations/discuss/27029/AC-Python-backtracking-iterative-solution-60-ms/119948


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Another method solve this problem by using stack
        stack, result = [], []
        x = 1
        while True:
            l = len(stack)
            if len(stack) == k:
                result.append(stack[:])
            if len(stack) == k or x > n:
                if not stack:
                    return result
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1


        # My method use backtracking
        def backtracking(nums, n, k):
            result = []
            if len(nums) == k:
                result.append(nums)
                return result
            elif nums and nums[-1] >= n:  # len(nums) must less than k
                return result
            start = nums[-1] + 1 if nums else 1
            for i in range(start, n + 1):
                result += backtracking(nums + [i], n, k)
            return result
        return backtracking([], n, k)
