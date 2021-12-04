
# 680. Valid Palindrome II

# https://leetcode.com/problems/valid-palindrome-ii/description/
# https://discuss.leetcode.com/topic/103982/python-easy-and-concise-solution


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s) // 2 and s[i] == s[-(i + 1)]: i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]


    # my version, following the problem logic
    #
    # flag = True
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     s_len = len(s)
    #     i, j = 0, s_len - 1
    #     while i < j:
    #         if s[i] != s[j]:
    #             if self.flag:
    #                 self.flag = False
    #                 return self.validPalindrome(s[i+1 : j+1]) or self.validPalindrome(s[i : j])
    #             else:
    #                 return False
    #         i += 1
    #         j -= 1
    #     return True
