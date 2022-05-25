
# 191. Number of 1 Bits

# https://leetcode.com/problems/number-of-1-bits/
# https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-%2B-even-faster-explained


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)  # Count the rightmost 1-bit and remove it
            ans += 1
        return ans
