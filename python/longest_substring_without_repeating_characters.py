
# 3. Longest Substring Without Repeating Characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        used = {}

        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[s[i]] = i
        return max_length
