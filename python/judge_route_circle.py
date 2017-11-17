
# 657. Judge Route Circle

# https://leetcode.com/problems/judge-route-circle/description/


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        right = moves.count('R')
        left = moves.count('L')
        up = moves.count('U')
        down = moves.count('D')
        if right == left and up == down:
            return True
        return False
