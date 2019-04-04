
# 48. Rotate Image

# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        max_index = n - 1
        for row in range(n // 2):
            for column in range(row, n - row - 1):
                # Rotate 90 degrees (clockwise)
                temp = matrix[row][column]
                matrix[row][column] = matrix[max_index - column][row]  # left -> top
                matrix[max_index - column][row] = matrix[max_index - row][max_index - column]  # bottom -> left
                matrix[max_index - row][max_index - column] = matrix[column][max_index - row]  # right -> bottom
                matrix[column][max_index - row] = temp  # top -> right
