
# 322. Coin Change

# https://leetcode.com/problems/coin-change/
# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Concise version
        MAX = float('inf')
        coin_counts = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                change = coin_counts[i - coin] + 1 if i - coin >= 0 else MAX
                coin_counts[i] = min(coin_counts[i], change)
        return coin_counts[-1] if coin_counts[-1] != MAX else -1
