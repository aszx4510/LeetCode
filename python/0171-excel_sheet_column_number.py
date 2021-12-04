
# 171. Excel Sheet Column Number

# https://leetcode.com/problems/excel-sheet-column-number/description/


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i, c in enumerate(reversed(s)):
            result += (ord(c) - ord('A') + 1) * pow(26, i)
        return result
