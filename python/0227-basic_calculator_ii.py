
# 227. Basic Calculator II

# https://leetcode.com/problems/basic-calculator-ii/
# https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        # All numbers are non-negative
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + (ord(s[i]) - ord('0'))
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1 * num)
                elif sign == '*':
                    temp = stack.pop() * num
                    stack.append(temp)
                else:
                    temp = stack.pop()
                    # Consider the situation that quotient is less than zero
                    if temp // num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = s[i]
                num = 0
        return sum(stack)
