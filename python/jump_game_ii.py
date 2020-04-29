
# 45. Jump Game II

# https://leetcode.com/problems/jump-game-ii/
# https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
# https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy/191474


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        steps, left, right = 0, 0, 0
        for i, num in enumerate(nums):
            right = max(right, i + num)
            if i == left:
                steps += 1
                left = right
            if left >= len(nums) - 1:
                break
        return steps
