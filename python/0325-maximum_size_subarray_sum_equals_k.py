
# 325. Maximum Size Subarray Sum Equals k

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77784/O(n)-super-clean-9-line-Java-solution-with-HashMap


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cnt, result = 0, 0
        prefix_sum_table = {0: 0}
        for i, num in enumerate(nums, start=1):
            cnt += num
            need = cnt - k

            if cnt == k:
                result = max(result, i)
            elif need in prefix_sum_table:
                result = max(result, i - prefix_sum_table[need])

            if cnt not in prefix_sum_table:
                prefix_sum_table[cnt] = i
        return result
