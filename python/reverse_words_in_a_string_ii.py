
# 186. Reverse Words in a String II

# https://leetcode.com/problems/reverse-words-in-a-string-ii/


class Solution(object):
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_array(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        reverse_array(0, len(s) - 1)

        previous = 0
        range_left, range_right = 0, 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse_array(previous, i - 1)
                previous = i + 1
            elif i == len(s) - 1:
                reverse_array(previous, i)
        return s
