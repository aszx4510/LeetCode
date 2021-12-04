
# 159. Longest Substring with At Most Two Distinct Characters

# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = {}
        left, right = 0, 0
        ans = 0
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            right += 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            ans = max(ans, right - left)
        return ans
