
# 1422. Maximum Score After Splitting a String

# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/598041/Clean-Python-3-one-pass


class Solution:
    def maxScore(self, s: str) -> int:
        zeros, minus, ones, result = 0, 0, 0, 0
        for ss in s[1:-1]:
            if ss == '1':
                ones += 1
                minus -= 1
            else:
                zeros += 1
            result = max(result, zeros + minus)
        return result + ones + (s[0] == '0') + (s[-1] == '1')


        # My method
        num_0, num_1 = s.count('0'), s.count('1')
        left = 1 if s[0] == '0' else 0
        right = num_1 - (1 if not left else 0)
        result = left + right
        for ss in s[1:-1]:
            # print(ss, left, right)
            if ss == '0':
                left += 1
            else:
                right -= 1
            result = max(result, left + right)
        return result
