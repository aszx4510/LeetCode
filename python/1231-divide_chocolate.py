
# 1231. Divide Chocolate

# https://leetcode.com/problems/divide-chocolate/
# https://leetcode.com/problems/divide-chocolate/discuss/408503/JavaC%2B%2BPython-Binary-Search


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left, right = 1, sum(sweetness) // (K + 1)
        while left < right:
            mid = (left + right + 1) // 2
            curr, n = 0, 0
            for s in sweetness:
                curr += s
                if curr >= mid:
                    n += 1
                    curr = 0

            # The curr is another cut
            if n > K:
                left = mid
            else:
                right = mid - 1
        return right
