
# 9. Palindrome Number 

# https://leetcode.com/problems/palindrome-number/description/
# reverse integer with only one extra integer space


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        # reverse half size to avoid overflow
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return (x == reverse or x == reverse // 10)
