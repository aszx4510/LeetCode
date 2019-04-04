
# 49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/
# https://leetcode.com/problems/group-anagrams/solution/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}
        for word in strs:
            anagram_dict.setdefault(tuple(sorted(word)), []).append(word)
        return list(anagram_dict.values())
