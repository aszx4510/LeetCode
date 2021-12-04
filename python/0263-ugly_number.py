
# 263. Ugly Number

# https://leetcode.com/problems/ugly-number/description/
# concise version
# https://discuss.leetcode.com/topic/21785/2-4-lines-every-language


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # concise version
        for p in 2, 3, 5:
            while num % p == 0 < num:  # num % p == 0 and 0 < num
                num /= p
        return num == 1


        # my method
        if num <= 0:
            return False
        if num <= 6:
            return True
        while num > 5:
            if num % 2 == 0:
                num /= 2
                continue
            elif num % 3 == 0:
                num /= 3
                continue
            elif num % 5 == 0:
                num /= 5
                continue
            return False  # num > 5 and num with a large prime factor at least
        return True
