
# 867. Transpose Matrix

# https://leetcode.com/problems/transpose-matrix/
# https://leetcode.com/problems/transpose-matrix/discuss/146797/C%2B%2BJavaPython-Easy-Understood


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)  # One line with Python built-in function


        # My version
        m, n = len(matrix), len(matrix[0])
        ans = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrix[j][i])
            ans.append(row)
        return ans
