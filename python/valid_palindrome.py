
# 125. Valid Palindrome

# https://leetcode.com/problems/valid-palindrome/description/
# https://leetcode.com/problems/valid-palindrome/discuss/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while right > left:
            while right > left and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
