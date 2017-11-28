
# 696. Count Binary Substrings

# https://leetcode.com/problems/count-binary-substrings/description/
# https://discuss.leetcode.com/topic/107108/python-easy-and-concise-solution-only-2-lines


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # super concise version
        s = list(map(len, s.replace('10', '1 0').replace('01', '0 1').split(' ')))  # split consecutive 1's and 0's
        return sum(min(a, b) for a, b in zip(s, s[1:]))


        # my version
        if not s:
            return 0
        prev_conti, conti = 0, 0
        ans = 0
        prev_c = s[0]

        for c in s:
            if c == prev_c:
                conti += 1
            else:
                ans += min(prev_conti, conti)
                prev_c = c
                prev_conti = conti
                conti = 1
        ans += min(prev_conti, conti)
        return ans
