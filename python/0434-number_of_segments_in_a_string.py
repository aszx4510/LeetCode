
# 434. Number of Segments in a String

# https://leetcode.com/problems/number-of-segments-in-a-string/description/
# https://discuss.leetcode.com/topic/70642/clean-java-solution-o-n


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):  # recognize the first non-space
                count += 1
        return count
