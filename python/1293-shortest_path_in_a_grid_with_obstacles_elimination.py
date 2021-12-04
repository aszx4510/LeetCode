
# 1293. Shortest Path in a Grid with Obstacles Elimination

# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Store all the state
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        if k >= (m + n - 2 - 1):
            return m + n - 2

        while queue:
            x, y, kk, steps = queue.popleft()
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + i, y + j
                if not (0 <= xx < m and 0 <= yy < n):
                    continue
                if grid[xx][yy] and kk > 0 and (xx, yy, kk - 1) not in visited:
                    visited.add((xx, yy, kk - 1))
                    queue.append((xx, yy, kk - 1, steps + 1))
                if not grid[xx][yy] and (xx, yy, kk) not in visited:
                    if xx == m - 1 and yy ==  n - 1:
                        return steps + 1
                    visited.add((xx, yy, kk))
                    queue.append((xx, yy, kk, steps + 1))
        return - 1


        # My method, it should be correct, but TLE
        def dfs(x, y, k, steps):
            nonlocal m, n, result, min_pos
            if result == min_pos:
                return
            if (not (0 <= x < m and 0 <= y < n)) or visited[x][y] or k < 0:
                return 
            if grid[x][y]:
                if k == 0:
                    return 
                k -= 1
            if x == m - 1 and y ==  n - 1:
                result = min(result, steps)
                return
            visited[x][y] = True
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(x + i, y + j, k, steps + 1)
            visited[x][y] = False
        m, n = len(grid), len(grid[0])
        min_pos = m + n - 2
        result = 10000
        visited = [[False] * n for _ in range(m)]

        dfs(0, 0, k, 0)
        return result if result <= 10000 else -1
