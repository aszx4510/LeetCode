
# 741. Cherry Pickup

# https://leetcode.com/problems/cherry-pickup/
# https://leetcode.com/problems/cherry-pickup/solution/


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Top-down
        def dp(row1, column1, column2):
            row2 = row1 + column1 - column2
            out_of_range = row1 == n or row2 == n or column1 == n or column2 == n
            if out_of_range or grid[row1][column1] == -1 or grid[row2][column2] == -1:
                return float('-inf')
            elif row1 == column1 == n - 1:
                return grid[row1][column1]
            elif memo[row1][column1][column2]:
                return memo[row1][column1][column2]
            else:
                ans = grid[row1][column1] + (column1 != column2) * grid[row2][column2]
                ans += max(dp(row1, column1 + 1, column2 + 1),  # Person 1 go right, Person 2 go right
                           dp(row1 + 1, column1, column2 + 1),  # Person 1 go down,  Person 2 go right
                           dp(row1, column1 + 1, column2),      # Person 1 go right, Person 2 go down
                           dp(row1 + 1, column1, column2))      # Person 1 go down,  Person 2 go down
            memo[row1][column1][column2] = ans
            return ans

        n = len(grid)
        memo = [[[None] * n for _1 in range(n)] for _2 in range(n)]
        return max(0, dp(0, 0, 0))


        # Bottom-up
        n = len(grid)
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for step in range(1, 2 * (n - 1) + 1):
            dp2 = [[float('-inf')] * n for _ in range(n)]
            for i in range(max(0, step - (n - 1)), min(n - 1, step) + 1):
                for j in range(max(0, step - (n - 1)), min(n - 1, step) + 1):
                    if grid[i][step - i] == -1 or grid[j][step - j] == -1:
                        continue
                    val = grid[i][step - i]
                    if i != j:
                        val += grid[j][step - j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i - 1, i) for pj in (j - 1, j)
                                    if pi >= 0 and pj >= 0)  # Four combination
            dp = dp2
        return max(0, dp[-1][-1])
