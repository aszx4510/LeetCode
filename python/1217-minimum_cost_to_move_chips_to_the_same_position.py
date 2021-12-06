
# 1217. Minimum Cost to Move Chips to The Same Position

# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ans = [0, 0]  # [even_num, odd_num]
        for p in position:
            ans[p % 2] += 1
        return min(ans)
