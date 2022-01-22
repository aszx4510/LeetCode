
# 877. Stone Game

# https://leetcode.com/problems/stone-game/
# https://leetcode.com/problems/stone-game/solution/
# https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Math
        # If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
        # he picks first piles[0], then Lee can pick either piles[1] or piles[n - 1].
        # Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

        # In the description, we know that sum(piles) is odd.
        # If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
        # If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.
        return True


        # Dynamic Programming, Time Complexity: O(N^2)
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (i - j) % 2
            if parity == 1:  # First player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:  # Deduct Alice's score from Bob's score
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
        return dp(0, len(piles) - 1) > 0
