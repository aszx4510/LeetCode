
# 74. Search a 2D Matrix

# https://leetcode.com/problems/search-a-2d-matrix/
# https://leetcode.com/problems/search-a-2d-matrix/discuss/26219/Binary-search-on-an-ordered-matrix


class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the matrix as a sorted list
        if not matrix or not matrix[0]:
            return False
        row, column = len(matrix), len(matrix[0])
        left, right = 0, row * column - 1
        while left <= right:
            mid = (left + right) // 2
            row_index, column_index = divmod(mid, column)
            if matrix[row_index][column_index] == target:
                return True
            elif matrix[row_index][column_index] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


        # My method, lower efficiency
        # if not matrix or not matrix[0]:
        #     return False
        # row_found = False
        # for row in range(len(matrix)):
        #     if matrix[row][-1] >= target:
        #         row_found = True
        #         break
        # if not row_found:
        #     return False
        
        # # Start binary search
        # left, right = 0, len(matrix[row]) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] > target:
        #         right = mid -1
        #     else:
        #         left = mid + 1
        # return False
