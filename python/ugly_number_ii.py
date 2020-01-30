
# 264. Ugly Number II

# https://leetcode.com/problems/ugly-number-ii/
# https://leetcode.com/problems/ugly-number-ii/discuss/69384/My-expressive-Python-solution


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # elegant code, Time Complexity: O(n)
        ugly = [1]
        i2, i3, i5 = 0, 0, 0

        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            min_ugly = min(u2, u3, u5)
            if min_ugly == u2:
                i2 += 1
            if min_ugly == u3:
                i3 += 1
            if min_ugly == u5:
                i5 += 1
            ugly.append(min_ugly)
            n -= 1
        return ugly[-1]


        # My method
        nums = [2, 3, 5]
        level, seen = {1}, {1}
        result = 1
        while len(seen) < n or (result and any(result > l for l in level)):
            level = set(num * l for num in nums for l in level) - seen
            seen.update(level)
            result = sorted(seen)[n - 1] if len(seen) >= n else None
        return result
