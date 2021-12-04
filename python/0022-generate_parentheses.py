
# 22. Generate Parentheses

# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, n):  # n is number of left parenthesis
            if n == 0:
                leak = s.count('(') - s.count(')')
                results.append(s + (')' * leak))
                return
            if s.count('(') > s.count(')'):
                backtrack(s + '(', n - 1)
                backtrack(s + ')', n)
            else:
                backtrack(s + '(', n - 1)
            return

        results = []
        backtrack('', n)
        return results
