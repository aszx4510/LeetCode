
# 66. Plus One

# https://leetcode.com/problems/plus-one/description/


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] < 9:  # if digit not equal to 9
                digits[i] += 1
                return digits
            digits[i] = 0

        # all digits are 9
        digits.insert(0, 1)
        return digits


        # number = 0
        # for digit in digits:
        #     number = number * 10 + digit
        # number += 1
        # answer = list()
        # while number > 0:
        #     answer.append(number % 10)
        #     number = number // 10
        # answer = list(reversed(answer))
        # return answer
