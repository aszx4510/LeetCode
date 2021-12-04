
# 258. Add Digits

# https://leetcode.com/problems/add-digits/description/
# https://discuss.leetcode.com/topic/28791/3-methods-for-python-with-explains


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        
        # N % 9 = a[0] + a[1] + ..a[n]
        # 9 % 9 = 0, so we can make (n - 1) % 9 + 1
        return ((num - 1) % 9) + 1
