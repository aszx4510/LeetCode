
# 198. House Robber

# https://leetcode.com/problems/house-robber/description/


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_rob = [0, 0]
        for num in nums:
            now_rob = max(prev_rob[0] + num, prev_rob[1])
            prev_rob = [prev_rob[1], now_rob]
        return prev_rob[1]
