
# 287. Find the Duplicate Number

# https://leetcode.com/problems/find-the-duplicate-number/
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation./75491


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Same question to 142. Linked List Cycle II
        # a + 2b + c = 2(a + b), a = c
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
