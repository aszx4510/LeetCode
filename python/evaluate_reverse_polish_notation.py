
# 150. Evaluate Reverse Polish Notation

# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: int(x + y),
            '-': lambda x, y: int(x - y),
            '*': lambda x, y: int(x * y),
            '/': lambda x, y: int(x / y)
        }
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()

                stack.append(operators[token](x, y))
        return int(stack.pop())
