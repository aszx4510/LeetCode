
# 453. Minimum Moves to Equal Array Elements

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
# https://discuss.leetcode.com/topic/66562/simple-one-liners


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I know another formula, but this version is better
        return sum(nums) - len(nums) * min(nums)
