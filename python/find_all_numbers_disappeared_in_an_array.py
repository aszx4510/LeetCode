
# 448. Find All Numbers Disappeared in an Array

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# https://discuss.leetcode.com/topic/68838/python-4-lines-with-short-explanation


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # concise version
        # reduce branch to get better performance
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [j + 1 for j in range(len(nums)) if nums[j] > 0]


        # my method is similar to #442
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        ans = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
