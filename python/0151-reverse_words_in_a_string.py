
# 151. Reverse Words in a String

# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution(object):
    def reverseWords(self, s: str) -> str:
        s = re.sub(r' +', ' ', s)
        return ' '.join(s.strip().split(' ')[::-1])
