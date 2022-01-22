
# 1510. Stone Game IV

# https://leetcode.com/problems/stone-game-iv/
# https://leetcode.com/problems/stone-game-iv/solution/


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Dynamic Programming, concise version
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for k in range(1, int(i ** 0.5) + 1):
                if not dp[i - k * k]:
                    dp[i] = True
                    break
        return dp[n]


        # Dynamic Programming, my version
        dp = [False] * (n + 1)
        dp[1] = True

        for i in range(2, n + 1):
            base = 1
            flag = False
            while base ** 2 <= i and not flag:
                if not dp[i - base ** 2]:
                    flag = True
                base += 1
            dp[i] = flag
        return dp[-1]

        
        # DFS with memoization, Time Limit Exceeded(?)
        @lru_cache
        def dfs(remain):
            if remain == 0:
                return False

            sqrt_root = int(remain ** 0.5)
            for i in range(1, sqrt_root + 1):
                if not dfs(remain - i * i):
                    return True
            return False
        return dfs(n)
