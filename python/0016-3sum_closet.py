
# 16. 3Sum Closest

# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 99999999999999
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                diff = (nums[i] + nums[left] + nums[right]) - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = nums[i] + nums[left] + nums[right]

                if diff > 0:
                    right -= 1
                elif diff < 0:
                    left += 1
                else:
                    return target
        return result
