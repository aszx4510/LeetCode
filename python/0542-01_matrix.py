
# 542. 01 Matrix

# https://leetcode.com/problems/01-matrix/
# https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Double Dynamic Programming
        m, n = len(mat), len(mat[0])

        # Start from top-left
        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    top = mat[i - 1][j] if i > 0 else math.inf
                    left = mat[i][j - 1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1
        # Start from bottom-right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] > 0:
                    bottom = mat[i + 1][j] if i < m - 1 else math.inf
                    right = mat[i][j + 1] if j < n - 1 else math.inf
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
        return mat


        # BFS
        m, n = len(mat), len(mat[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Mark as not processed yet

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dirs[i][0], c + dirs[i][1]
                if not (0 <= nr < m and 0 <= nc < n) or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
