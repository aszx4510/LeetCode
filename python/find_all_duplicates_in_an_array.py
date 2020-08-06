
# 442. Find All Duplicates in an Array

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(idx + 1)
            nums[idx] *= -1
        return
