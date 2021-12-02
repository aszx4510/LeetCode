
# 283. Move Zeroes

# https://leetcode.com/problems/move-zeroes/description/
# https://discuss.leetcode.com/topic/24716/simple-o-n-java-solution-using-insert-index
# https://discuss.leetcode.com/topic/24716/simple-o-n-java-solution-using-insert-index/6


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointer
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        nums[left:] = [0] * (n - left)
        return


        # two pointer
        current = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[current]
                nums[current] = nums[i]
                current += 1
                nums[i] = temp  # nums[i] = 0
        return


        # mentain insert index
        if nums is None or len(nums) == 0:
            return
        insert_index = 0
        for num in nums:  # here maybe violate the rule 1: You must do this in-place without making a copy of the array.
            if num != 0:
                nums[insert_index] = num
                insert_index += 1
        while insert_index < len(nums):
            nums[insert_index] = 0
            insert_index += 1
        return


        # my method, "del" need too much operations
        i, j = 0, len(nums) - 1
        while i < j:  # the last element can be ignored
            print(i, nums[i], j, nums[j])
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
                i -= 1
                j -= 1
            i += 1
        return
