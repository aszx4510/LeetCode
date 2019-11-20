
# 201. Bitwise AND of Numbers Range

# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
