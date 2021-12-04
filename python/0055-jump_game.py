
# 55. Jump Game

# https://leetcode.com/problems/jump-game/
# https://leetcode.com/problems/jump-game/solution/


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        # My new version code
        max_jump, now = 0, 0
        while now < len(nums) and now <= max_jump:
            max_jump = max(max_jump, now + nums[now])
            now += 1
        return max_jump >= (len(nums) - 1)


        # Old version
        if not nums:
            return True
        checked, far_index = 0, 0
        while checked < len(nums) and checked <= far_index:
            if far_index >= len(nums) - 1:
                return True
            far_index = max(far_index, checked + nums[checked])
            checked += 1
        return False
