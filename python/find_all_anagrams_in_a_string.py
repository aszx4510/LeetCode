
# 438. Find All Anagrams in a String

# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def check(i):
            if len(ans) != len(occur):
                return
            for alhpabet, cnt in ans.most_common():
                if alhpabet not in occur or occur[alhpabet] != cnt:
                    return
            result.append(i)
            return

        n = len(p)
        result = []
        ans, occur = Counter(p), dict()

        # Concise version
        left = 0
        for right in range(len(s)):
            occur[s[right]] = occur.get(s[right], 0) + 1
            if right - left >= n:
                occur[s[left]] = occur.get(s[left], 0) - 1
                if occur[s[left]] == 0:
                    del occur[s[left]]
                left += 1
            check(left)
        return result


        # Another version
        first = Counter(s[:n - 1])
        occur.update(first)
        for i in range(n - 1, len(s)):
            occur[s[i]] = occur.get(s[i], 0) + 1
            if i != n - 1:
                temp = s[i - n]
                occur[temp] = occur.get(temp, 0) - 1
                if occur[temp] == 0:
                    del occur[temp]
            check(i - (n - 1))
        return result
