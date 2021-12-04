
# 118. Pascal's Triangle

# https://leetcode.com/problems/pascals-triangle/description/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        triangle = [[1]]
        for i in range(1, numRows):
            row = list()
            for j in range(0, len(triangle[i - 1])):
                if j == 0:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                if j == len(triangle[i - 1]) - 1:  # the last round
                    row.append(1)
            triangle.append(row)
        return triangle
