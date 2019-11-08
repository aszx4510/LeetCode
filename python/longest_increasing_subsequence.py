
# 300. Longest Increasing Subsequence

# https://leetcode.com/problems/longest-increasing-subsequence/
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time Complexity: O(nlogn)
        tail = []
        for num in nums:
            left, right = 0, len(tail)
            while left != right:
                mid = (left + right) // 2
                if num > tail[mid]:
                    left = mid + 1
                else:
                    right = mid
            if left >= len(tail):
                tail.append(num)
            else:
                tail[left] = num
        return len(tail)


        # # My method by usnig DP, Time Complexity: O(n^2)
        # if not nums:
        #     return 0

        # dp = []
        # for num in nums:
        #     max_result = 0
        #     for i in range(len(dp)):
        #         if num > nums[i]:
        #             max_result = max(dp[i], max_result)
        #     dp.append(max_result + 1)
        # return max(dp)
