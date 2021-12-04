
# 137. Single Number II

# https://leetcode.com/problems/single-number-ii/
# https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
# https://cloud.tencent.com/developer/article/1131945


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a
