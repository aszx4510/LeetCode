
# 645. Set Mismatch

# https://leetcode.com/problems/set-mismatch/description/
# https://discuss.leetcode.com/topic/96807/python-straightforward-with-explanation


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # a little math
        nums_sum = (len(nums) + 1) * len(nums) // 2
        no_repeat_sum = sum(set(nums))
        miss = nums_sum - no_repeat_sum
        repeat = sum(nums) - no_repeat_sum
        return repeat, miss


        # straightforward
        count = [0] * len(nums)
        for num in nums:
            count[num - 1] += 1
        repeat, miss = -1, -1
        for i in range(len(count)):
            if count[i] > 1:  # count[i] == 2
                repeat = i + 1
            elif count[i] <= 0:  # count[i] == 0
                miss = i + 1
        return repeat, miss
