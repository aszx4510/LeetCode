
# 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/description/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs or len(strs[0]) == 0:  # check empty strs
            return prefix
            
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            same = True
            for string in strs:
                if i > len(string) - 1:
                    same = False
                    break
                
                if prefix != string[0:i + 1]:
                    same = False
                    break
             
            if not same:
                prefix = prefix[0:-1]
                break
        return prefix
