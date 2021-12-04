
# 476. Number Complement

# https://leetcode.com/problems/number-complement/
# https://leetcode.com/problems/number-complement/discuss/96009/Simple-Python
# https://leetcode.com/problems/number-complement/discuss/96103/maybe-fewest-operations


class Solution:
    def findComplement(self, num: int) -> int:
        # Another method
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num


        # My version
        n, num_bk = 0, num
        while num != 0:
            num //= 2
            n += 1
        ones = (1 << n) - 1
        return num_bk ^ ones
