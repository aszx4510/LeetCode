
# 387. First Unique Character in a String

# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos, seen = {}, set()
        for i, ss in enumerate(s):
            if ss not in seen:
                pos[ss] = i
                seen.add(ss)
            elif ss in pos.keys():
                pos.pop(ss)
        return list(pos.values())[0] if pos else -1
