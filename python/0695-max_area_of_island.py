
# 695. Max Area of Island

# https://leetcode.com/problems/max-area-of-island/description/
# https://discuss.leetcode.com/topic/106370/easy-python


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + sum([dfs(i+x, j+y) for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1))])
            return 0
        
        areas = [dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        return max(areas)
