
# 274. H-Index

# https://leetcode.com/problems/h-index/
# https://leetcode.com/problems/h-index/discuss/70810/A-Clean-O(N)-Solution-in-Java/73014


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c > n:
                cnt[n] += 1
            else:
                cnt[c] += 1

        ans = 0
        for i in reversed(range(n + 1)):
            ans += cnt[i]
            if ans >= i:
                return i
        return 0
