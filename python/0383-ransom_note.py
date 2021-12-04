
# 383. Ransom Note

# https://leetcode.com/problems/ransom-note/description/


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = dict()
        for c in magazine:
            count[c] = count.setdefault(c, 0) + 1
        for c in ransomNote:
            count[c] = count.setdefault(c, 0) - 1
            if count[c] < 0:
                return False
        return True
