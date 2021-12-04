
# 918. Maximum Sum Circular Subarray

# https://leetcode.com/problems/maximum-sum-circular-subarray/
# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass


class Solution(object):
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = 0
        max_result, min_result = float('-inf'), float('inf')
        max_sum, min_sum = 0, 0
        for a in A:
            max_sum = max(a, max_sum + a)
            min_sum = min(a, min_sum + a)
            max_result = max(max_result, max_sum)
            min_result = min(min_result, min_sum)
            total += a
        return max(max_result, total - min_result) if max_result > 0 else max_result
