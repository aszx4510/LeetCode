
# 441. Arranging Coins

# https://leetcode.com/problems/arranging-coins/description/
# https://leetcode.com/problems/arranging-coins/discuss/162814/Python-O(1)-Math-Solution-Fully-Explained
# https://leetcode.com/problems/arranging-coins/discuss/92274/JAVA-Clean-Code-with-Explanations-and-Running-Time-2-Solutions


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Mathematics
        return int((math.sqrt(8 * n + 1)-1)/2)


        # Binary Search, O(log(n))
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2

            if (mid + 1) * mid <= 2 * n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


        # My old method, O(log(n))
        base = 1
        total = 0
        while total <= n:
            total += base
            base += 1
        return base - 2
