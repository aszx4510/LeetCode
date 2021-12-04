
# 17. Letter Combinations of a Phone Number

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Backtracking
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for c in mapping[next_digits[0]]:
                    backtrack(combination + c, next_digits[1:])

        output = []
        if digits:
            backtrack('', digits)
        return output


        # My lower efficiency method
        # mapping = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz',
        # }

        # if not digits:
        #     return []

        # result = ['']
        # next_level = []
        # for d in digits:
        #     for r in result:
        #         for c in mapping[d]:
        #             next_level.append( r + c)
        #     result = next_level.copy()
        #     next_level = []
        # return result
