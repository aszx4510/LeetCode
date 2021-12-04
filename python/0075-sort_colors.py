
# 75. Sort Colors

# https://leetcode.com/problems/sort-colors/
# https://leetcode.com/problems/sort-colors/solution/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Three pointers
        zero_flag, two_flag = 0, len(nums) - 1
        current = 0
        while current < len(nums) and current <= two_flag:
            if nums[current] == 0:
                nums[current] = nums[zero_flag]
                nums[zero_flag] = 0
                zero_flag += 1
                current += 1
            elif nums[current] == 2:
                nums[current] = nums[two_flag]
                nums[two_flag] = 2
                two_flag -= 1
            else:
                current += 1
