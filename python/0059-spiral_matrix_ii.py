
# 59. Spiral Matrix II

# https://leetcode.com/problems/spiral-matrix-ii/
# Similar with #54
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

class Solution(object):
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral_coordinate(row1, row2, column1, column2):
            for column in range(column1, column2 + 1):
                yield row1, column
            for row in range(row1 + 1, row2):
                yield row, column2
            if row1 < row2 and column1 < column2:
                for column in range(column2, column1, -1):
                    yield row2, column
                for row in range(row2, row1, -1):
                    yield row, column1

        result = [[0] * n for i in range(n)]
        row1, row2 = 0, n - 1
        column1, column2 = 0, n - 1
        count = 1
        while row1 <= row2 and column1 <= column2:
            for row, column in spiral_coordinate(row1, row2, column1, column2):
                result[row][column] = count
                count += 1
            row1 += 1
            row2 -= 1
            column1 += 1
            column2 -= 1
        return result
