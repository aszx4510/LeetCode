
# 461. Hamming Distance

# https://leetcode.com/problems/hamming-distance/
# https://leetcode.com/problems/hamming-distance/discuss/94697/Python-1-line-49ms


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # My method
        xor = x ^ y
        result = 0
        while xor:
            result += xor & 0x1
            xor >>= 1
        return result


        # One line version
        return bin(x ^ y).count('1')
