
# 293. Flip Game

# https://leetcode.com/problems/flip-game/


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        result = []
        p = 0
        while p < len(s) - 1:
            if s[p] == s[p + 1] == '+':
                result.append(s[:p] + '--' + s[p + 2:])
            p += 1
        return result
