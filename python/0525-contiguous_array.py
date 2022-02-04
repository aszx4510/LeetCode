
# 525. Contiguous Array

# https://leetcode.com/problems/contiguous-array/
# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, ans = 0, 0
        # Log first appearance
        table = {0: 0}  # table = {cnt, index}
        for i, num in enumerate(nums, start=1):
            cnt += num if num else -1

            p = table.setdefault(cnt, i)
            ans = max(ans, i - p)
        return ans
