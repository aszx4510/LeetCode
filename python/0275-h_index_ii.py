
# 275. H-Index II

# https://leetcode.com/problems/h-index-ii/
# https://leetcode.com/problems/h-index-ii/discuss/71063/Standard-binary-search


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Binary search version
        n = len(citations)
        left, right = 0, len(citations)
        while left <= right and left :
            mid = (left + right) // 2
            if mid == n:
                return 0
            if citations[mid] == (n - mid):
                return citations[mid]
            elif citations[mid] > (n - mid):
                right = mid - 1
            else:
                left = mid + 1
        return n - (right + 1)


        # My method, Time Complexity: O(n)
        ans = 0
        for i, v in enumerate(citations[::-1], start=1):
            if v >= i:
                ans = i
        return ans
