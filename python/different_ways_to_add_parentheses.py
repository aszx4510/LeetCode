
# 241. Different Ways to Add Parentheses

# https://leetcode.com/problems/different-ways-to-add-parentheses/
# https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer).


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]

        result = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        result.append(self.helper(l, r, input[i]))
        return result


    def helper(self, m, n, op):
        if op == '+':
            return m + n
        elif op == '-':
            return m - n
        else:
            return m * n
