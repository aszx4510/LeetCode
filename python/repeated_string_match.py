
# 686. Repeated String Match

# https://leetcode.com/problems/repeated-string-match/description/
# https://discuss.leetcode.com/topic/105618/intuitive-python-2-liner
# https://discuss.leetcode.com/topic/105579/c-4-lines-o-m-n-o-1-and-7-lines-kmp-o-m-n-o-n


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B) // len(A))  # # Equal to ceil(len(b) / len(a))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1
