
# 1480. Running Sum of 1d Array

# https://leetcode.com/problems/running-sum-of-1d-array/
# https://leetcode.com/problems/running-sum-of-1d-array/discuss/686276/C%2B%2BPython-Partial-Sum


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)


        # My version
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
