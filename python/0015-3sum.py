
# 15. 3Sum

# https://leetcode.com/problems/3sum/
# https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):  # Fix one parameter
            # Skip identical number, it's the same situation
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
                else:  # is zero
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip identical number, it's the same situation
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
