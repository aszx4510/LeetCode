
# 1009. Complement of Base 10 Integer

# https://leetcode.com/problems/complement-of-base-10-integer/


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1
        i = 1
        while i <= N:
            i <<= 1
        return (i - 1) ^ N
