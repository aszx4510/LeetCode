
# 29. Divide Two Integers

# https://leetcode.com/problems/divide-two-integers/
# https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                # Shift left 1-bit, equal to i *= 2
                i <<= 1
                temp <<= 1

        if not positive:
            result = -result
        return min(max(-2147483648, result), 2147483647)  # Check overflow
