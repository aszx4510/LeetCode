
# 18. 4Sum

# https://leetcode.com/problems/4sum/
# https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_n_sum(nums, target, n, result, results):
            if len(nums) < n or n < 2:
                return

            if n == 2:  # 2-pointer to solve 2-sum
                left, right = 0, len(nums) - 1
                while left < right:
                    temp = nums[left] + nums[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
            else:
                for i in range(len(nums) - n + 1):
                    # Take advantages of sorted list
                    if target < nums[i] * n or target > nums[-1] * n:
                        break
                    if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                        find_n_sum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        find_n_sum(nums, target, 4, [], results)
        return results
