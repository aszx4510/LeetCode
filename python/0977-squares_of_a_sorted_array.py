
# 977. Squares of a Sorted Array

# https://leetcode.com/problems/squares-of-a-sorted-array/
# https://leetcode.com/problems/squares-of-a-sorted-array/solution/


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                square = nums[left] ** 2
                left += 1
            else:
                square = nums[right] ** 2
                right -= 1

            ans[i] = square
        return ans


        # # My method
        # left, right = 0, len(nums) - 1
        # ans = []

        # while left <= right:
        #     if abs(nums[left]) >= abs(nums[right]):
        #         ans.append(nums[left] ** 2)
        #         left += 1
        #     else:
        #         ans.append(nums[right] ** 2)
        #         right -= 1
        # return ans[::-1]
