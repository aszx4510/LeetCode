
# 219. Contains Duplicate II

# https://leetcode.com/problems/contains-duplicate-ii/description/
# https://discuss.leetcode.com/topic/22444/python-concise-solution-with-dictionary



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # only record the last position
        position = dict()
        for i, value in enumerate(nums):
            if value in position and i - position[value] <= k:
                return True
            position[value] = i
        return False


        # my method with bad efficiency
        # positions = dict()
        # for i in range(len(nums)):
        #     if nums[i] in positions:
        #         for pos in positions[nums[i]]:
        #             if i - pos <= k:
        #                 return True
        #     positions.setdefault(nums[i], list()).append(i)
        # return False

