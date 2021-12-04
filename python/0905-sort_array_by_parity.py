
# 905. Sort Array By Parity

# https://leetcode.com/problems/sort-array-by-parity/
# https://leetcode.com/problems/sort-array-by-parity/discuss/803633/Python-O(n)-In-place-partition-explained


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # Inplace method, Space Complexity: O(1)
        start, end = 0, len(A) - 1

        while start <= end:
            if A[start] % 2 == 0:
                start += 1
            else:
                A[start], A[end] = A[end], A[start]
                end -= 1
        return A


        # My method, Space Complexity: O(n)
        evens, odds = [], []
        for a in A:
            if a % 2 == 0:
                evens.append(a)
            else:
                odds.append(a)
        evens.extend(odds)
        return evens
