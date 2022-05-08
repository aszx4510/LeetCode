
# 3. Longest Substring Without Repeating Characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0, 0
        used = {}  # {alphabet: position}

        for right in range(len(s)):
            alphabet = s[right]
            if alphabet in used and left <= used[alphabet]:
                left = used[alphabet] + 1
            else:
                max_len = max(max_len, right - left + 1)
            used[alphabet] = right
        return max_len
