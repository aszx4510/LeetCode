
# 322. Coin Change

# https://leetcode.com/problems/coin-change/
# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
# https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution/81426


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS
        level = seen = {0}
        count = 0
        while level:
            if amount in level:
                return count
            # Check all possible amount in level
            level = {a + c for a in level for c in coins if a + c <= amount} - seen
            seen.update(level)
            count += 1
        return -1


        # Concise version for DP
        MAX = float('inf')
        coin_counts = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                change = coin_counts[i - coin] + 1 if i - coin >= 0 else MAX
                coin_counts[i] = min(coin_counts[i], change)
        return coin_counts[-1] if coin_counts[-1] != MAX else -1
