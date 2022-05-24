
# 994. Rotting Oranges

# https://leetcode.com/problems/rotting-oranges/


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        step = 2
        while queue:
            i, j = queue.popleft()
            for d in range(len(dirs)):
                ni, nj = i + dirs[d][0], j + dirs[d][1]
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] == 1:
                    grid[ni][nj] = grid[i][j] + 1
                    step = max(step, grid[ni][nj])
                    queue.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return step - 2
