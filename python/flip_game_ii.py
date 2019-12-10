
# 294. Flip Game II

# https://leetcode.com/problems/flip-game-ii/
# https://leetcode.com/problems/flip-game-ii/discuss/73998/Python-Solution-3-Lines/278965
# https://leetcode.com/problems/flip-game-ii/discuss/73958/Memoization%3A-3150ms-greater-130ms-greater-44ms-(Python)


class Solution:
    def canWin(self, s: str) -> bool:
        def helper(s):
            if s in memo:
                return memo[s]

            for i in range(len(s) - 1):
                if s[i] == s[i+1] =='+' and not helper(s[:i] + '--' + s[i+2:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        memo = {}
        return helper(s)
