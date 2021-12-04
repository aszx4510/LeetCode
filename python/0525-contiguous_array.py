
# 525. Contiguous Array

# https://leetcode.com/problems/contiguous-array/
# https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, result = 0, 0
        # Log first appearance
        table = {0: 0}  # table = {cnt, index}
        for i, num in enumerate(nums, start=1):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1

            if cnt in table:
                result = max(result, i - table[cnt])
            else:
                table[cnt] = i
        return result
