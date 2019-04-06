
# 55. Jump Game

# https://leetcode.com/problems/jump-game/
# https://leetcode.com/problems/jump-game/solution/


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        checked, far_index = 0, 0
        while checked < len(nums) and checked <= far_index:
            if far_index >= len(nums) - 1:
                return True
            far_index = max(far_index, checked + nums[checked])
            checked += 1
        return False
