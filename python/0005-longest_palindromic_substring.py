
# 5. Longest Palindromic Substring

# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j, s):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]

        # It's a optional check
        s_length = len(s)
        if s_length <= 1:
            return s

        longest_palidrome = ''
        for i in range(s_length):
            # Odd cases: 'aba'
            palidrome = helper(i, i, s)
            if len(palidrome) >= len(longest_palidrome):
                longest_palidrome = palidrome

            # Even cases: 'abba'
            palidrome = helper(i, i + 1, s)
            if len(palidrome) >= len(longest_palidrome):
                longest_palidrome = palidrome
        return longest_palidrome
