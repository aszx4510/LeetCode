
# 409. Longest Palindrome

# https://leetcode.com/problems/longest-palindrome/
# https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)
