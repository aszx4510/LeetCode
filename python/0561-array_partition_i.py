
# 561. Array Partition I

# https://leetcode.com/problems/array-partition-i/description/
# https://discuss.leetcode.com/topic/87270/python-1-line-sorting-is-accepted


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
