
# 279. Perfect Squares

# https://leetcode.com/problems/perfect-squares/
# https://leetcode.com/problems/perfect-squares/solution/
# https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS
# https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution/81426


class Solution:
    def numSquares(self, n: int) -> int:
        # Dynamic Programming
        max_square = int(math.sqrt(n))
        square_nums = [pow(i, 2) for i in range(0, max_square + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for square in square_nums:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]


        # Greedy
        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums

            for square in square_nums:
                if is_divided_by(n - square, count - 1):
                    return True
            return False

        max_square = int(math.sqrt(n))
        square_nums = [pow(i, 2) for i in range(0, max_square + 1)]
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


        # Greedy + BFS
        max_square = int(math.sqrt(n))
        square_nums = [pow(i, 2) for i in range(0, max_square + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()

            for remainder in queue:
                for square in square_nums:
                    if remainder == square:
                        return level  # Find the node
                    elif remainder < square:
                        break
                    else:
                        next_queue.add(remainder - square)

            queue = next_queue
        return level


        # Greedy + BFS, concise version
        max_square = int(math.sqrt(n))
        square_nums = [pow(i, 2) for i in range(0, max_square + 1)]
        level = seen = {0}
        count = 0
        while level:
            if n in level:
                return count
            level = {amount + square for amount in level for square in square_nums if amount + square <= n} - seen
            seen.update(level)
            count += 1
        return -1


        # Mathematics, that's impossible
        # Lagrange's four-square theorem
        def is_square(n):
            sq = int(math.sqrt(n))
            return sq * sq == n

        # four-square and three-square theorems
        # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
        # n = 4^a * (8*b + 7)
        while n & 3 == 0:
            n >>= 2  # reducing the 4^k factor from number

        if (n & 7) == 7:  # Mod 8
            return 4

        if is_square(n):
            return 1

        max_square = int(math.sqrt(n))
        for i in range(1, max_square + 1):
            if is_square(n - i * i):
                return 2
        return 3
