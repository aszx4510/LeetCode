
# 1015. Smallest Integer Divisible by K

# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/1655649/Python3-Less-Math-More-Intuition-or-2-Accepted-Solutions-or-Intuitive


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # A number divisible by 2 can only end with 0, 2, 4, 6 or 8
        # A number divisible by 5 can only end with 0 or 5
        if not k % 2 or not k % 5:
            return -1

        # General version, Time Limit Exceeded
        n = length = 1
        while True:
            if not n % k:
                return length
            length += 1
            n = n * 10 + 1


        # Math
        r = length = 1
        while True:
            r = r % k
            if not r:
                return length
            length += 1
            r = r * 10 + 1
