
# 240. Search a 2D Matrix II

# https://leetcode.com/problems/search-a-2d-matrix-ii/
# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        row, col = 0, n - 1
        while col >= 0 and row < m:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
