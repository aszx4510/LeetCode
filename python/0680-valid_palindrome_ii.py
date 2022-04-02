
# 680. Valid Palindrome II

# https://leetcode.com/problems/valid-palindrome-ii/description/
# https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left: right], s[left + 1: right + 1]
                return one == one[:: -1] or two == two[:: -1]
            left, right = left + 1, right - 1
        return True


    # my version, following the problem logic
    #
    # flag = True
    # def validPalindrome(self, s: str) -> bool:
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
