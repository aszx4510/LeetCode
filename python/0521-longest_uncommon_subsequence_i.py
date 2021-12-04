
# 521. Longest Uncommon Subsequence I 

# https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
# https://discuss.leetcode.com/topic/85029/python-simple-explanation


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # concise version
        if a == b:
            return -1
        return max(len(a), len(b))


        # my method
        if len(b) > len(a):
            a, b = b, a
        if a in b:
            return -1
        else:
            return len(a)
