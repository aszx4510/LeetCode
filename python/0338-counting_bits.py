
# 338. Counting Bits

# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        base = 1
        for i in range(1, num + 1):
            if i == base:
                result[i] = 1
                base *= 2  # base <<= 1
                continue

            result[i] = 1 + result[i - (base // 2)]
        return result
