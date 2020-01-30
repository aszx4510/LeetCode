
# 313. Super Ugly Number

# https://leetcode.com/problems/super-ugly-number/
# https://leetcode.com/problems/super-ugly-number/discuss/76301/Python-generators-on-a-heap


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Black magic!
        ugly = [1]
        merged = heapq.merge(*map(lambda p: (u * p for u in ugly), primes))
        uniqued = (u for u, _ in itertools.groupby(merged))
        for x in itertools.islice(uniqued, n - 1):
            ugly.append(x)
        return ugly[-1]


        # Magic...
        ugly = [1]
        def gen(prime):
            for u in ugly:
                print(ugly, f'--calling from {prime}')
                print(u * prime)
                yield u * prime

        # Got 3 generators from map
        # Merge 3 generators by heapq
        merged = heapq.merge(*map(gen, primes))
        while len(ugly) < n:
            u = next(merged)
            if u != ugly[-1]:
                ugly.append(u)
        return ugly[-1]


        # Similar with 264: Ugly Number II
        ugly = [1]
        indice = [0] * len(primes)

        while n > 1:
            ugly_values = [ugly[i] * p for p, i in zip(primes, indice)]
            min_ugly = min(ugly_values)
            for i, u in enumerate(ugly_values):
                if min_ugly == u:
                    indice[i] += 1
            ugly.append(min_ugly)
            n -= 1
        return ugly[-1]
