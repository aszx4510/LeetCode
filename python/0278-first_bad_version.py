
# 278. First Bad Version

# https://leetcode.com/problems/first-bad-version/
# https://leetcode.com/problems/first-bad-version/discuss/71333/1-liner-in-Ruby-Python/203147


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
