
# 67. Add Binary

# https://leetcode.com/problems/add-binary/description/
# https://leetcode.com/problems/add-binary/solution/
# https://leetcode.com/problems/add-binary/discuss/24500/an-accepted-concise-python-recursive-solution-10-lines


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Bit manipulation
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]  # Remove the prefix '0b'


        # Recursive method
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'


        # My method
        # i = len(a) - 1
        # j = len(b) - 1
        # sum = 0
        # carry = 0
        # answer = ''
        # while i >= 0 or j >= 0:
        #     sum = carry
        #     if i >= 0:
        #         sum += ord(a[i]) - ord('0')
        #         i -= 1
        #     if j >= 0:
        #         sum += ord(b[j]) - ord('0')
        #         j -= 1

        #     answer += str(sum % 2)
        #     carry = sum // 2

        # if carry != 0:
        #     answer += '1'
        # return answer[::-1]  # reverse the string
