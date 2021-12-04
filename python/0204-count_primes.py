
# 204. Count Primes

# https://leetcode.com/problems/count-primes/description/
# https://discuss.leetcode.com/topic/14036/fast-python-solution/4


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [True] * n
        primes[:2] = [False] * 2
        for base in range(2, int((n - 1) ** 0.5) + 1):
            if primes[base]:
                primes[base ** 2 :: base] = [False] * len(primes[base ** 2 :: base])
        return sum(primes)
