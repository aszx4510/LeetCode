
# 65. Valid Number

# https://leetcode.com/problems/valid-number/
# https://leetcode.wang/leetCode-65-Valid-Number.html


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        number = False
        exponent, need_exponent_num = False, False
        dot = False
        for i in range(0, len(s)):
            if s[i].isdigit():
                number = True
                need_exponent_num = False
            elif s[i] == 'e':
                if exponent or not number:
                    return False
                else:
                    exponent = True
                    need_exponent_num = True
            elif s[i] == '.':
                if dot or exponent:
                    return False
                else:
                    dot = True
            elif s[i] in ['+', '-']:
                if i != 0 and s[i-1] != 'e':
                    return False
            else:
                return False
        if need_exponent_num:
            return False
        return number
