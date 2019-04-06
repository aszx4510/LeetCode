
# 60. Permutation Sequence

# https://leetcode.com/problems/permutation-sequence/
# https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation

import math


class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        # My method, backtracking
        def backtracking(numbers, n, k):
            if k == 1:
                return ''.join([str(x) for x in numbers])
            count, index = 0, 0
            fac = math.factorial(n - 1)
            while count < k and index < n:
                count += fac
                index += 1
            count -= fac
            index -= 1
            return str(numbers.pop(index)) + backtracking(numbers, n - 1, k - count)
        
        return backtracking([x for x in range(1, n + 1)], n, k)


        # Another method of iteration
        # numbers = [x for x in range(1, n + 1)]
        # result = ''
        # k -= 1
        # while n > 0:
        #     n -= 1
        #     index, k = divmod(k, math.factorial(n))
        #     result += str(numbers.pop(index))
        # return result
