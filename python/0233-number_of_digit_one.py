
# 233. Number of Digit One

# https://leetcode.com/problems/number-of-digit-one/
# https://blog.csdn.net/xudli/article/details/46798619
# https://leetcode.com/problems/number-of-digit-one/discuss/64381/4%2B-lines-O(log-n)-C%2B%2BJavaPython
# https://www.cnblogs.com/grandyang/p/5459846.html


class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0

        m = 1
        while m <= n:
            a, b = divmod(n, m)
            # if (a + 8) >= 10, it means a > 1
            ans += (a + 8) // 10 * m + ((b + 1) if a % 10 == 1 else 0)
            m *= 10
        return ans
