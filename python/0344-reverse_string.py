
# 344. Reverse String

# https://leetcode.com/problems/reverse-string/description/
# http://yehnan.blogspot.tw/2015/04/python.html


class Solution(object):
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
