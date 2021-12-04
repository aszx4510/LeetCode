
# 120. Triangle

# https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle.pop(0)
        for ladder in triangle:
            next_dp = []
            n = len(ladder)
            next_dp.append(dp[0] + ladder[0])
            for i in range(1, n - 1):
                next_dp.append(min(dp[i - 1], dp[i]) + ladder[i])
            next_dp.append(dp[-1] + ladder[-1])
            dp = next_dp
        return min(dp)
