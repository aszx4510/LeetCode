
# 459. Repeated Substring Pattern

# https://leetcode.com/problems/repeated-substring-pattern/description/
# https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s is 'XX', ss is 'XXXX'
        # ss[1 : -1] is 'YXXY', we can find out the s in 'YXXY'
        if not s:
            return False
        ss = (s + s)[1 : -1]
        return ss.find(s) != -1
