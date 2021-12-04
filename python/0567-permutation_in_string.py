
# 567. Permutation in String

# https://leetcode.com/problems/permutation-in-string/
# https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding Window, same as #438
        s1_num = [ord(x) - ord('a') for x in s1]
        s2_num = [ord(x) - ord('a') for x in s2]

        target, window = [0] * 26, [0] * 26
        for x in s1_num:
            target[x] += 1

        for i, x in enumerate(s2_num):
            window[x] += 1
            if i >= len(s1):
                window[s2_num[i - len(s1)]] -= 1
            if window == target:
                return True
        return False
