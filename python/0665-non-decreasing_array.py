
# 665. Non-decreasing Array

# https://leetcode.com/problems/non-decreasing-array/description/
# https://discuss.leetcode.com/topic/101147/python-extremely-easy-to-understand


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Copy from the submission
        not_first, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                if not_first:
                    return False
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    prev = nums[i]
                not_first = True
            else:
                prev = nums[i]
        return True


        # Discussion version, slower becuase the sorting
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        # Avoid the bug when the key element at first or last
        return one == sorted(one) or two == sorted(two)
