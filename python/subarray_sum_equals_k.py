
# 560. Subarray Sum Equals K

# https://leetcode.com/problems/subarray-sum-equals-k/
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
# Similar to #525: Contiguous Array


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        total_count = {total: 1}
        result = 0
        for num in nums:
            total += num
            leak = total - k
            result += total_count.get(leak, 0)
            total_count[total] = total_count.get(total, 0) + 1
        return result
