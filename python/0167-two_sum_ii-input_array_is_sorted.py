
# 167. Two Sum II - Input array is sorted

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            temp = numbers[left] + numbers[right]
            
            if temp == target:
                return [left + 1, right + 1]
            elif temp < target:
                left += 1
            else:
                right -= 1
        return
