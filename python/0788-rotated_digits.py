
# 788. Rotated Digits

# https://leetcode.com/problems/rotated-digits/description/
# https://leetcode.com/problems/rotated-digits/discuss/116547/Easily-Understood-Java-Solution


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_valid(n):
            valid = False
            while n > 0:
                last = n % 10
                # 2 and 5 rotate to each other; 6 and 9 rotate to each other -> good number
                # 3, 4, 7 are invalid after rotated -> not good number
                # 0, 1, and 8 rotate to themselves -> doesn't matter
                if last == 2 or last == 5 or last == 6 or last == 9:
                    valid = True
                if last == 3 or last == 4 or last == 7:
                    return False
                n = n // 10
            return valid

        count = 0
        for num in range(1, N + 1):
            if is_valid(num):
                count += 1
        return count
