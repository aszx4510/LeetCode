
# 54. Spiral Matrix

# https://leetcode.com/problems/spiral-matrix/
# https://leetcode.com/problems/spiral-matrix/solution/
# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral_coords(row1, row2, column1, column2):
            for column in range(column1, column2 + 1):
                yield row1, column
            for row in range(row1 + 1, row2 + 1):
                yield row, column2
            if row1 < row2 and column1 < column2:  # Check if need to go back
                for column in range(column2 - 1, column1, -1):
                    yield row2, column
                for row in range(row2, row1, -1):
                    yield row, column1

        if not matrix:
            return []
        result = []
        row1, row2 = 0, len(matrix) - 1
        column1, column2 = 0, len(matrix[0]) - 1
        while row1 <= row2 and column1 <= column2:
            for row, column in spiral_coords(row1, row2, column1, column2):
                result.append(matrix[row][column])
            row1 += 1
            row2 -= 1
            column1 += 1
            column2 -= 1
        return result

        # Oh my God
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
