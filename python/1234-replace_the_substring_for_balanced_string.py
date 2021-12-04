
# 1234. Replace the Substring for Balanced String

# https://leetcode.com/problems/replace-the-substring-for-balanced-string/
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/JavaC++Python-Sliding-Window/368403

class Solution:
    def balancedString(self, s: str) -> int:
        n, limit = len(s), len(s) // 4
        c_count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for c in s:
            c_count[c] += 1
        if max(c_count.values()) == min(c_count.values()):
            return 0

        left, right = 0, 0
        result = n
        while right < n:
            c_count[s[right]] -= 1
            right += 1
            while left < n and all(limit >= c_count[c] for c in 'QWER'):
                result = min(result, right - left)
                c_count[s[left]] += 1
                left += 1
        return result
