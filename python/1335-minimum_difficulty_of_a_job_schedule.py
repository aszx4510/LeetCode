
# 1335. Minimum Difficulty of a Job Schedule

# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp method
        n, inf = len(jobDifficulty), int(1e8)
        if n < d:
            return -1
        # dp[d][k] means min difficulty from `jobDifficulty[k:]` in `d` days
        dp = [[inf] * n + [0] for _ in range(d + 1)]
        for day in range(1, d + 1):
            for i in range(n - day + 1):
                max_num = 0  # Record the max number in jobDifficulty[i:]
                for j in range(i , n - day + 1):
                    max_num = max(max_num, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], max_num + dp[day - 1][j + 1])
        return dp[d][0]


        # dfs method, it's same as dp when we use functolls.lru_cache
        n = len(jobDifficulty)
        if n < d:
            return -1

        @functools.lru_cache(maxsize=None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, max_num = float('inf'), 0
            for j in range(i, n - d + 1):
                max_num = max(max_num, jobDifficulty[j])
                res = min(res, max_num + dfs(j + 1, d - 1))
            return res

        return dfs(0, d)
