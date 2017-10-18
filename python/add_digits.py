
# 258. Add Digits

# https://leetcode.com/problems/add-digits/description/
# https://discuss.leetcode.com/topic/28791/3-methods-for-python-with-explains
# N % 9 = a[0] + a[1] + ..a[n]
# 9 % 9 = 0, so we can make (n - 1) % 9 + 1


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        return ((num - 1) % 9) + 1
