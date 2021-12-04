
# 205. Isomorphic Strings

# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t_map= {}
        for ss, tt in zip(s, t):
            if ss not in s2t_map.keys():
                if tt in s2t_map.values():
                    return False
                s2t_map[ss] = tt
            if tt != s2t_map[ss]:
                return False
        return True
