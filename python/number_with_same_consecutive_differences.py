
# 967. Numbers With Same Consecutive Differences

# https://leetcode.com/problems/numbers-with-same-consecutive-differences/


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def dfs(prefix, remaining):
            if remaining == 0:
                if prefix[0] != '0' or prefix == '0':
                    result.append(prefix)
                return
            if len(prefix) == 0:
                for i in range(10):
                    dfs(str(i), remaining - 1)
            else:
                last_number = int(prefix[-1])
                numbers = set((last_number + K, last_number - K))
                for num in list(numbers):
                    if 0 <= num <= 9:
                        dfs(prefix + str(num), remaining - 1)

        result = []
        dfs('', N)
        return result
