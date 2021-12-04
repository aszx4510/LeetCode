
# 278. First Bad Version

# https://leetcode.com/problems/first-bad-version/
# https://leetcode.com/problems/first-bad-version/discuss/71333/1-liner-in-Ruby-Python/203147


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
