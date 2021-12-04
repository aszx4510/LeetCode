
# 485. Max Consecutive Ones

# https://leetcode.com/problems/max-consecutive-ones/description/


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive = 0
        consecutive = 0
        for num in nums:
            if num == 1:
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            elif num == 0:
                consecutive = 0
        return max_consecutive
