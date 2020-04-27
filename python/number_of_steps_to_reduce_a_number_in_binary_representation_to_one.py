
# 1404. Number of Steps to Reduce a Number in Binary Representation to One

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/discuss/573402/C%2B%2B-0ms-6.5MB


class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        added = False
        for ss in s[: 0 : -1]:
            if ss == '0':
                steps += 1
                if added:
                    steps += 1
            else:
                steps += 1
                if not added:
                    steps += 1
                    added = True
        if added:
            steps += 1
        return steps

        # # Same as first version
        # n = len(s)
        # for i in range(1, n + 1):
        #     if s[i * -1] == '1':
        #         break
        # if i == n:
        #     return n - 1
        # subs = s[: n - i]
        # carry = 1 if subs else 0
        # n0, n1 = subs.count('0'), subs.count('1')
        # return n0 * 2 + n1 * 1 + i + carry


        # # My version
        # steps = 0
        # while s != '1':
        #     # print(s, steps)
        #     i = -1
        #     if s[i] == '0':
        #         while s[i] == '0':
        #             i -= 1
        #         s = s[: i + 1]
        #         steps += abs(i + 1)
        #     else:
        #         while s[i] == '1' and abs(i) < len(s):
        #             i -= 1
        #         if abs(i) == len(s):
        #             s = '1' + '0' * len(s)
        #         else:
        #             s = s[: i] + '1' + '0' *(abs(i) - 1)
        #         steps += 1
        # return steps
