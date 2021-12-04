
# 217. Contains Duplicate

# https://leetcode.com/problems/contains-duplicate/description/
# https://discuss.leetcode.com/topic/14730/possible-solutions


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False


        # check list
        # Submission Result: Time Limit Exceeded
        # check = list()
        # for num in nums:
        #     if num in check:
        #         return True
        #     else:
        #         check.append(num)
        # return False


        # count number
        # Submission Result: Time Limit Exceeded
        # for num in nums:
        #     if nums.count(num) >= 2:
        #         return True
        # return False
