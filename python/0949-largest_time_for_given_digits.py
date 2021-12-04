
# 949. Largest Time for Given Digits

# https://leetcode.com/problems/largest-time-for-given-digits/
# https://leetcode.com/problems/largest-time-for-given-digits/discuss/200693/JavaPython-3-11-liner-O(64)-w-comment-6-ms.


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for t1, t2, t3, t4 in itertools.permutations(sorted(A, reverse=True)):
            if (t1, t2) < (2, 4) and t3 < 6:
                return f'{t1}{t2}:{t3}{t4}'
        return ''
