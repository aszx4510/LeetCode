
# 392. Is Subsequence

# https://leetcode.com/problems/is-subsequence/
# https://leetcode.com/problems/is-subsequence/discuss/87258/2-lines-Python


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use iterator
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

        if len(s) > len(t):
            return False
        i, n = 0, len(t)
        for ss in s:
            if i >= n:
                return False
            while t[i] != ss:
                i += 1
                if i >= n:
                    return False
            i += 1
        return True
