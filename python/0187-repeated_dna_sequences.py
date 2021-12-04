
# 187. Repeated DNA Sequences

# https://leetcode.com/problems/repeated-dna-sequences/


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s_len = len(s)
        dna_set, result = set(), set()

        left, right = 0, 10
        while right <= s_len:
            if s[left:right] in dna_set:
                result.add(s[left:right])
            else:
                dna_set.add(s[left:right])
            left += 1
            right += 1
        return list(result)
