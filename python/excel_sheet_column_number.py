
# 171. Excel Sheet Column Number

# https://leetcode.com/problems/excel-sheet-column-number/description/


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for i, ch in enumerate(reversed(s)):
            number += (ord(ch) - ord('A') + 1) * (26 ** i)
        return number
