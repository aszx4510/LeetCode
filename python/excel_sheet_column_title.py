
# 168. Excel Sheet Column Title

# https://leetcode.com/problems/excel-sheet-column-title/description/
# https://discuss.leetcode.com/topic/6214/my-1-lines-code-in-java-c-and-python


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return '' if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
