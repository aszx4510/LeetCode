
# 36. Valid Sudoku

# https://leetcode.com/problems/valid-sudoku/
# https://leetcode.com/problems/valid-sudoku/discuss/15472/Short%2BSimple-Java-using-Strings


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    row_text = board[i][j] + ' in row ' + str(i)
                    column_text = board[i][j] + ' in column ' + str(j)
                    block_text = board[i][j] + ' in block ' + str(i // 3) + '-' + str(j // 3)

                    if row_text in seen or column_text in seen or block_text in seen:
                        return False
                    seen.add(row_text)
                    seen.add(column_text)
                    seen.add(block_text)
        return True
