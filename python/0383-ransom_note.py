
# 383. Ransom Note

# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count_letters(string: str):
            d = defaultdict(int)
            for s in string:
                d[s] += 1
            return d
        ransom_dict = count_letters(ransomNote)
        magazine_dict = count_letters(magazine)
        for letter, number in ransom_dict.items():
            # if not (letter in magazine_dict or number <= magazine[letter])
            if not number <= magazine_dict[letter]:
                return False
        return True
