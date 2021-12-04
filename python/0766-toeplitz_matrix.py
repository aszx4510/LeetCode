
# 766. Toeplitz Matrix

# https://leetcode.com/problems/toeplitz-matrix/description/


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row - 1):
            for j in range(column - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
