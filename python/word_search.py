
# 79. Word Search

# https://leetcode.com/problems/word-search/
# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Better efficiency without additional space
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and word[0] == board[i][j]:
                temp = board[i][j]
                board[i][j] = '#'
                flag = dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:]) or \
                       dfs(board, i, j + 1, word[1:]) or dfs(board, i, j - 1, word[1:])
                board[i][j] = temp
                return flag
            return False
    
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False


        # My method with lower efficiency
        def search(path, i, j):
            w = word[len(path)]
            if board[i][j] == w:
                path = path + [str(i) + '-' + str(j)]
                if len(path) == len(word):
                    return True
                flag = False
                for x, y in zip(dir_x, dir_y):
                    new_i = i + y
                    new_j = j + x
                    check = str(new_i) + '-' + str(new_j)

                    if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and check not in path :
                        flag = flag or search(path, new_i, new_j)
                return flag
            else:
                return False
        # up, down, right, left
        dir_x = [0, 0, 1, -1]
        dir_y = [-1, 1, 0, 0]

        for i in range(len(board)):
            for j in range(len(board[0])):
                result = search([], i, j)
                if result:
                    return True
        return False
