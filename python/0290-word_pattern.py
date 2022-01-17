
# 290. Word Pattern

# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # Concise version
        parts = s.split(' ')
        if len(pattern) != len(parts):
            return False

        mapping, inverse = {}, {}
        for i, (p, w) in enumerate(zip(pattern, parts)):
            if mapping.get(p, -1) != inverse.get(w, -1):
                return False
            mapping[p] = inverse[w] = i
        return True


        # My version
        mapping, inverse = {}, {}
        if len(pattern) != len(str.split(' ')):
            return False

        for s, word in zip(pattern, str.split(' ')):
            if s in mapping and mapping[s] != word:
                return False
            if word in inverse and inverse[word] != s:
                return False
            mapping[s] = word
            inverse[word] = s
        return True
