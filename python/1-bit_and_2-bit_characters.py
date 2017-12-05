
# 717. 1-bit and 2-bit Characters

# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bit1_flag = False
        bit2_flag = False
        for bit in bits:
            if bit == 1:
                bit2_flag = not bit2_flag
            if bit == 0:
                if bit2_flag:
                    bit2_flag = not bit2_flag
                    bit1_flag = False
                else:
                    bit1_flag = True
        return bit1_flag
