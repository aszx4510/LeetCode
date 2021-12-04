
# 678. Valid Parenthesis String

# https://leetcode.com/problems/valid-parenthesis-string/
# https://leetcode.com/problems/valid-parenthesis-string/discuss/107577/Short-Java-O(n)-time-O(1)-space-one-pass


class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for ss in s:
            if ss == '(':
                low += 1
                high += 1
            elif ss == ')':
                if low > 0:
                    low -= 1
                high -= 1
            elif ss == '*':
                if low > 0:
                    low -= 1
                high += 1

            if high < 0:
                return False
        return low == 0
