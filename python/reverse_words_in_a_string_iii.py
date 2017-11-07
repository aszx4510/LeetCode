
# 557. Reverse Words in a String III

# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# https://discuss.leetcode.com/topic/85882/1-line-ruby-python


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # concise version
        return ' '.join(s.split()[::-1])[::-1]


        # my method
        tokens = s.split(' ')
        for i in range(len(tokens)):
            tokens[i] = tokens[i][::-1]
        return ' '.join(tokens)
