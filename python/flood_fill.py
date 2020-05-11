
# 733. Flood Fill

# https://leetcode.com/problems/flood-fill/
# https://leetcode.com/problems/flood-fill/discuss/109604/Easy-Python-DFS-(no-need-for-visited)!!!


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(row, col, color):
            if not (0 <= row < len(image) and 0 <= col < len(image[0])):
                return
            if not visited[row][col] and image[row][col] == color:
                image[row][col] = newColor
                visited[row][col] = True
                # Concise syntax
                [dfs(row + x, col + y, color) for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                # dfs(row - 1, col, color)
                # dfs(row + 1, col, color)
                # dfs(row, col - 1, color)
                # dfs(row, col + 1, color)

        visited = [[False] * len(image[0]) for r in range(len(image))]
        dfs(sr, sc, image[sr][sc])
        return image
