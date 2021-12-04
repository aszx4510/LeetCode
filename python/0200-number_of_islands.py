
# 200. Number of Islands

# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if 0 <= x < row and 0 <= y < column:
                if grid[x][y] == '1':
                    # https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
                    grid[x][y] = '#'
                    dfs(x + 1, y)
                    dfs(x - 1, y)
                    dfs(x, y + 1)
                    dfs(x, y - 1)
                    return True
            return False

        if not grid:
            return 0
        row, column = len(grid), len(grid[0])

        ans = 0
        for x in range(row):
            for y in range(column):
                found = dfs(x, y)
                if found:
                    ans += 1
        return ans
