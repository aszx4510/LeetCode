
# 73. Set Matrix Zeroes

# https://leetcode.com/problems/set-matrix-zeroes/
# https://leetcode.com/problems/set-matrix-zeroes/solution/


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_column_is_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_column_is_zero = True
            for j in range(1, len(matrix[0])):  # First column are already checked
                if matrix[i][j] == 0:  # Make the flags
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_column_is_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
