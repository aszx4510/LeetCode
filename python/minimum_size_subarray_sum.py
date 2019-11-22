
# 209. Minimum Size Subarray Sum

# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 0
        min_len = len(nums)

        temp_sum = nums[right]
        found = False
        while True:
            if temp_sum >= s:
                min_len = min(min_len, right - left + 1)
                temp_sum -= nums[left]
                left +=1
                found = True
            else:
                right += 1
                if right >= len(nums):
                    break
                temp_sum += nums[right]
        return min_len if found else 0
