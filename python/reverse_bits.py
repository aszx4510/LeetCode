
# 190. Reverse Bits

# https://leetcode.com/problems/reverse-bits/
# https://leetcode.com/problems/reverse-bits/solution/


class Solution:
    def reverseBits(self, n: int) -> int:
        result, power = 0, 31
        while n:
            result += (n & 1) << power
            n >>= 1
            power -= 1
        return result


        # My method, it's not really good
        n_bin = bin(n)
        n_rev = n_bin[:1:-1]
        leading_zero = 32 - len(n_rev)  # 32-bit
        result = n_rev +  '0' * leading_zero
        return int(result, 2)
