
# 213. House Robber II

# https://leetcode.com/problems/house-robber-ii/
# https://leetcode.com/problems/house-robber-ii/discuss/59944/Twice-pass-solution-C%2B%2B


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        # Skip first one
        prev_rob = [0, 0]
        for i in range(1, len(nums)):
            now_rob = max(prev_rob[0] + nums[i], prev_rob[1])
            prev_rob = [prev_rob[1], now_rob]

        # Skip last one
        prev_rob2 = [0, 0]
        for i in range(len(nums) - 1):
            now_rob = max(prev_rob2[0] + nums[i], prev_rob2[1])
            prev_rob2 = [prev_rob2[1], now_rob]

        return max(prev_rob[1], prev_rob2[1])
