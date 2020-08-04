
# 342. Power of Four

# https://leetcode.com/problems/power-of-four/
# https://leetcode.com/problems/power-of-four/solution/


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # Math
        return num > 0 and log2(num) % 2 == 0


        # My method
        if num < 0:
            return False
        binary = bin(num)[2:]

        if binary.count('1') == 1 and binary.count('0') % 2 == 0:
            return True
        return False
