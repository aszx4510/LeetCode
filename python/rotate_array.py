
# 189. Rotate Array

# https://leetcode.com/problems/rotate-array/description/
# https://discuss.leetcode.com/topic/14341/easy-to-read-java-solution
# https://stackoverflow.com/questions/22257249/how-do-i-reverse-a-sublist-in-a-list-in-place


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # ignore the loop
        nums = self.reverse_sublist(nums, 0, n)
        nums = self.reverse_sublist(nums, 0, k)
        nums = self.reverse_sublist(nums, k, n)
        return


    def reverse_sublist(self, lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        return lst
