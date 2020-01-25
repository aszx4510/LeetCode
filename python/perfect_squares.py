
# 279. Perfect Squares

# https://leetcode.com/problems/perfect-squares/
# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
# https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution/81426


class Solution(object):
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        max_num = int(math.sqrt(n) // 1)
        possible_squares = {num * num for num in range(1, max_num + 1)}
        level = seen = {0}
        count = 0
        while level:
            if n in level:
                return count
            level = {amount + square for amount in level for square in possible_squares if amount + square <= n} - seen
            seen.update(level)
            count += 1
        return -1
