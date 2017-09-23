
# 20. Valid Parentheses

# https://leetcode.com/problems/valid-parentheses/description/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        corresponding_dict = {']': '[', '}': '{', ')': '('}

        stack = []
        for ch in s:
            if ch in corresponding_dict.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                pop = stack.pop()
                if pop != corresponding_dict[ch]:
                    return False
        return not stack
