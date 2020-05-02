
# 771. Jewels and Stones

# https://leetcode.com/problems/jewels-and-stones/


class Solution(object):
    def numJewelsInStones(self, J: str, S: str) -> int:
        seen = set(J)
        result = 0
        for s in S:
            result += s in seen
        return result
