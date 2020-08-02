
# 520. Detect Capital

# https://leetcode.com/problems/detect-capital/description/
# https://discuss.leetcode.com/topic/79951/python-has-useful-methods


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
