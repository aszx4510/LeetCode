
# 416. Partition Equal Subset Sum

# https://leetcode.com/problems/partition-equal-subset-sum/
# https://leetcode.com/problems/partition-equal-subset-sum/solution/
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total  = sum(nums)
        if total % 2 != 0:
            return False

        n = len(nums)
        subset_sum = total // 2

        # # Brute Force, Time complexity: O(n^2), Time Limit Exceeded
        # def dfs(nums, n, subset_sum):
        #     if subset_sum == 0:
        #         return True
        #     if n == 0 or subset_sum < 0:
        #         return False
        # 
        #     return dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum)
        # return dfs(nums, n, subset_sum)


        # Dynamic Programming, Top Down
        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False

            return dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum)
        return dfs(tuple(nums), n, subset_sum)


        # Dynamic Programming, Bottom Up
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[-1][-1]


        # Dynamic Programming, Bottom Up 1D array version
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
                if dp[-1]:
                    return True
        return False
