
# 268. Missing Number

# https://leetcode.com/problems/missing-number/description/
# https://discuss.leetcode.com/topic/24535/4-line-simple-java-bit-manipulate-solution-with-explaination
# The basic idea is to use XOR operation. We all know that a ^ b ^ b = a.


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i, value in enumerate(nums):
            xor = xor ^ i ^ value
        return xor ^ (i + 1)
