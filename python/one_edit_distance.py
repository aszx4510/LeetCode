
# 161. One Edit Distance

# https://leetcode.com/problems/one-edit-distance/
# https://leetcode.com/problems/one-edit-distance/discuss/50101/Easy-understood-Java-solution


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Concise version
        def isOneModify(s, t):
            edit = 0
            for i in range(n):
                if s[i] != t[i]:
                    edit += 1
            return edit == 1

        def isOneInsert(s, t):
            m = len(s)
            for i in range(m):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True  # Insert the last character

        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False

        if m == n:
            return isOneModify(s, t)

        if m > n:
            return isOneInsert(t, s)
        else:
            return isOneInsert(s, t)


        # # My method
        # m, n = len(s), len(t)
        # if abs(m - n) > 1:
        #     return False

        # if m == n:
        #     edit = 0
        #     for i in range(n):
        #         if s[i] != t[i]:
        #             edit += 1
        #     return True if edit == 1 else False

        # if m > n:
        #     m, n = n, m
        #     s, t = t, s
        # edit = 0
        # for i in range(n):
        #     if i == n - 1 and edit == 0:
        #         return True
        #     if s[i - edit] != t[i]:
        #         edit += 1
        #         if edit > 1:
        #             return False
        # return True if edit == 1 else False
