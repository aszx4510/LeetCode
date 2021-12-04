
# 136. Single Number

# https://leetcode.com/problems/single-number/
# https://leetcode.com/problems/single-number/solution/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a XOR 0 = a
        # a XOR a = 0
        ans = 0
        for num in nums:
            ans ^= num  # XOR
        return ans
