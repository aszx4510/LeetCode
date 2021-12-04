
# 463. Island Perimeter

# https://leetcode.com/problems/island-perimeter/description/
# https://discuss.leetcode.com/topic/68786/clear-and-easy-java-solution


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Mathematics, faster and use less memory
        if not grid:
            return 0
        island, neighbor = 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    island += 1
                    if i != m - 1 and grid[i + 1][j]:
                        neighbor += 1
                    if j != n - 1 and grid[i][j + 1]:
                        neighbor += 1
        return island * 4 - neighbor * 2


        # My method, DFS
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == '#':
                return 0
            grid[i][j] = '#'
            p = [dfs(i + x, j + y) for x, y in zip((1, -1, 0, 0), (0, 0, 1, -1))]
            return sum(p)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += dfs(i, j)
        return result
