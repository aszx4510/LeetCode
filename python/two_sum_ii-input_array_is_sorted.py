
# 167. Two Sum II - Input array is sorted

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            diff = target - numbers[left]
            while left < right and numbers[right] >= diff:
                if numbers[right] == diff:
                    return [left + 1, right + 1]
                right -= 1
            left += 1
        return None
