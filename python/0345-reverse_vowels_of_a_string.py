
# 345. Reverse Vowels of a String

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# https://discuss.leetcode.com/topic/43463/1-2-lines-python-ruby


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

