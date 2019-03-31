
# 1018. Binary Prefix Divisible By 5

# https://leetcode.com/contest/weekly-contest-130/problems/binary-prefix-divisible-by-5/


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        base = 0
        for a in A:
            base = base * 2 + a
            result.append(True if base % 5 == 0 else False)
        return result
