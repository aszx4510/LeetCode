
# 1631. Path With Minimum Effort

# https://leetcode.com/problems/path-with-minimum-effort/
# https://leetcode.com/problems/path-with-minimum-effort/solution/
# https://leetcode.com/problems/path-with-minimum-effort/discuss/909002/JavaPython-3-3-codes%3A-Binary-Search-Bellman-Ford-and-Dijkstra-w-brief-explanation-and-analysis.


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')] * n for _ in range(m)]
        efforts[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col)
        while heap:
            effort, x, y = heapq.heappop(heap)
            if effort > efforts[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return effort
            for r, c in ((x, y + 1), (x, y - 1), (x + 1, y),(x - 1, y)):
                if 0 <= r < m and 0 <= c < n:
                    next_effort = max(effort, abs(heights[r][c] - heights[x][y]))
                    if efforts[r][c] > next_effort:
                        efforts[r][c] = next_effort
                        heapq.heappush(heap, (efforts[r][c], r, c))
