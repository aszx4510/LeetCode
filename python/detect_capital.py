
# 520. Detect Capital

# https://leetcode.com/problems/detect-capital/description/
# https://discuss.leetcode.com/topic/79951/python-has-useful-methods


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # all upper
        # all lower
        # first character is upper
        return word.isupper() or word.islower() or word.istitle()
