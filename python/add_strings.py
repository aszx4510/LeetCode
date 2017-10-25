
# 415. Add Strings

# https://leetcode.com/problems/add-strings/description/
# https://discuss.leetcode.com/topic/62344/python-7-line-52ms-1-liner-for-fun
# a concise code to solve this problem


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        import itertools
        # z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')  # Python 2
        z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')  # Python 3
        res, carry, zero2 = [], 0, 2 * ord('0')
        for i in z:
            current_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
            res.append(str(current_sum % 10))
            carry = current_sum // 10
        return ('1' if carry else '') + ''.join(res[::-1])
