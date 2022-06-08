
# 1332. Remove Palindromic Subsequences

# https://leetcode.com/problems/remove-palindromic-subsequences/
# https://leetcode.com/problems/remove-palindromic-subsequences/solution/


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Check palindrome with custom method
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if not s:
            return 0
        if is_palindrome(s):
            return 1
        return 2


        # Python built-in method to check palindrome
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
