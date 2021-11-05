
# 611. Valid Triangle Number

# https://leetcode.com/problems/valid-triangle-number/
# https://leetcode.com/problems/valid-triangle-number/solution/
# https://leetcode.com/problems/valid-triangle-number/discuss/1339248/Python-sort-%2B-2-pointers-solution-explained


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums, n, ans = sorted(nums), len(nums), 0
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right - left)
                    right -= 1
                else:
                    left += 1
        return ans

        # # Linear Scan: Time Complexity: O(n^2)
        # nums, n, ans = sorted(nums), len(nums), 0
        # for i in range(n - 2):
        #     if nums[i] == 0:
        #         continue

        #     k = i + 2
        #     for j in range(i + 1, n - 1):
        #         while k < n and nums[i] + nums[j] > nums[k]:
        #             k += 1
        #         ans += k - j - 1
        # return ans


        # # Brute Force :Time Complexity: O(n^3), Time Limit Exceeded
        # nums = sorted(nums)
        # ans = 0
        # len_n = len(nums)
        # for i in range(len_n - 2):
        #     for j in range(i + 1, len_n - 1):
        #         for k in range(j + 1, len_n):
        #             if nums[i] + nums[j] > nums[k]:
        #                 ans += 1
        # return ans
