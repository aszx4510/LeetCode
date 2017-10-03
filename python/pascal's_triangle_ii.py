
# 119. Pascal's Triangle II

# https://leetcode.com/problems/pascals-triangle-ii/description/
# https://discuss.leetcode.com/topic/15559/very-simple-python-solution


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row