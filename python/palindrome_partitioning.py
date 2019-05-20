
# 131. Palindrome Partitioning

# https://leetcode.com/problems/palindrome-partitioning/
# https://leetcode.com/problems/palindrome-partitioning/discuss/41963/Java:-Backtracking-solution./40320
# https://leetcode.com/problems/palindrome-partitioning/discuss/41982/Java-DP-%2B-DFS-solution


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Dynamic programming and backtracking
        def dfs(s, position, parts):
            if position == len(s):
                result.append(parts[:])
                return
            for i in range(position, len(s)):
                if dp[position][i]:
                    parts.append(s[position:i + 1])
                    dfs(s, i + 1, parts)
                    parts.pop()

        result = []
        # Store all palindromes
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                # Check s[j:i]
                if s[i:i + 1] == s[j:j + 1] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        dfs(s, 0, [])
        return result


        # # Normal backtracking and palindrome inspection
        # def is_palindrome(s, low, high):
        #     while low < high:
        #         if s[low:low + 1] != s[high - 1:high]:
        #             return False
        #         low += 1
        #         high -= 1
        #     return True

        # def dfs(s, position, parts):
        #     if position == len(s):
        #         result.append(parts[:])
        #         return
        #     for i in range(position, len(s)):
        #         if is_palindrome(s, position, i + 1):
        #             parts.append(s[position:i + 1])
        #             dfs(s, i + 1, parts)
        #             parts.pop()

        # result = []
        # dfs(s, 0, [])
        # return result
