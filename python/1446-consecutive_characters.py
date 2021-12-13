
# 1446. Consecutive Characters

# https://leetcode.com/problems/consecutive-characters/
# https://leetcode.com/problems/consecutive-characters/discuss/635241/Python-One-line


class Solution:
    def maxPower(self, s: str) -> int:
        ans, consecutive = 0, 1
        temp = ''
        for c in s:
            if c == temp:
                consecutive += 1
            else:
                temp = c
                consecutive = 1
            ans = max(ans, consecutive)
        return ans


        # One-line version
        import itertools
        return max(len(list(b)) for a, b in itertools.groupby(s))
