
# 551. Student Attendance Record I

# https://leetcode.com/problems/student-attendance-record-i/description/


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use regex
        import re
        x = re.search('LLL|.*A.*A.*', s)
        return True if x is None else False


        # my initial solution
        count_A = 0
        continue_late = 0
        for c in s:
            if c == 'A':
                if count_A >= 1:
                    return False
                count_A += 1
                continue_late = 0
            elif c == 'L':
                if continue_late >= 2:
                    return False
                else:
                    continue_late += 1
            else:
                continue_late = 0
        return True
