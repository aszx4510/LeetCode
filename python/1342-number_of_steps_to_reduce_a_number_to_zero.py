
# 1342. Number of Steps to Reduce a Number to Zero

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Counting bits
        ans = 0
        binary = bin(num)[2:]  # Remove '0b'

        for b in binary:
            if b == '1':
                ans += 2
            else:
                ans += 1
        # Remove the over counting of last bit
        return ans - 1
        
