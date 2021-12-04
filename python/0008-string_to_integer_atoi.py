
# 8. String to Integer (atoi)

# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        num, sign = 0, 1
        for i in range(0, len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')

                # overflow
                if sign < 0 and num > 2147483648:
                    return -2147483648
                elif sign > 0 and num > 2147483647:
                    return 2147483647
            elif i == 0 and s[i] in ['+', '-']:
                if len(s) == 1:
                    return 0
                elif s[i] == '-':
                    sign = -1
            elif not s[i].isdigit():
                break
        return num * sign
