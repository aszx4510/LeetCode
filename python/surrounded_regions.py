
# 130. Surrounded Regions

# https://leetcode.com/problems/surrounded-regions/
# https://leetcode.com/problems/surrounded-regions/discuss/41612/A-really-simple-and-readable-C%2B%2B-solutionuff0conly-cost-12ms


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if i >= 0 and i < row and j >= 0 and j < column and board[i][j] == 'O':
                board[i][j] = 'N'
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
            return

        if not board:
            return
        row, column = len(board), len(board[0])

        # Start from edge
        # Region can't be surrounded if there is a way from edge
        for i in range(row):
            dfs(i, 0)
            dfs(i, column - 1)
        for j in range(column):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(column):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return


        # # My method has a low efficiency
        # def check_region(i, j):
        #     if board[i][j] == 'X' or checked[i][j]:
        #         return True
        #     path.append((i, j))
        #     checked[i][j] = True
        #     # Keep checking
        #     up = check_region(i - 1, j) if i - 1 >= 0 else False
        #     down = check_region(i + 1, j) if i + 1 < row else False
        #     left = check_region(i, j - 1) if j - 1 >= 0 else False
        #     right = check_region(i, j + 1) if j + 1 < column else False
        #     return up and down and left and right

        # if not board:
        #     return
        # row, column = len(board), len(board[0])
        # checked = [[False] * column for _ in range(row)]

        # for i in range(1, row - 1):
        #     for j in range(1, column - 1):
        #         if checked[i][j]:
        #             continue
        #         path = []
        #         if check_region(i, j):
        #             for path_i, path_j in path:
        #                 board[path_i][path_j] = 'X'
        # return
