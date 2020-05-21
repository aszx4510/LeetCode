
# 1277. Count Square Submatrices with All Ones

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # One-line version
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
        return sum(map(sum, matrix))


        # Concise version
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                result += matrix[i][j]
        return result


        # My version
        result = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if matrix[i - 1][j - 1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                result += dp[i][j]
        return result
