
# 994. Rotting Oranges

# https://leetcode.com/problems/rotting-oranges/


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        def rot(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return
            if grid[i][j] == 1 and (i, j) not in queue:
                queue.append((i, j))

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        step = -1
        while queue and fresh:
            temp_queue = queue.copy()
            queue.clear()
            step += 1
            while temp_queue:
                i, j = temp_queue.pop(0)
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh -= 1
                for x, y in direction:
                    rot(i + x, j + y)

        # Avoid there are all rotten oranges in the original grid
        return max(0, step) if fresh == 0 else -1
