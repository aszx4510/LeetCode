
# 463. Island Perimeter

# https://leetcode.com/problems/island-perimeter/description/
# https://discuss.leetcode.com/topic/68786/clear-and-easy-java-solution


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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
