
# 134. Gas Station

# https://leetcode.com/problems/gas-station/
# https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gap = [g - c for g, c in zip(gas, cost)]
        n = len(gas)
        i, tank, total = 0, 0, 0
        start = 0
        while i < n:
            tank += gap[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
            i += 1
        return start if total + tank >= 0 else -1


        # # My method has a low efficiency
        # gap = [g - c for g, c in zip(gas, cost)]
        # n = len(gas)
        # start = 0
        # a_round = False
        # while start < n and (not a_round):
        #     end = (start - 1 + n) % n
        #     current_sum = gap[start]
        #     while current_sum >= 0 and start != end:
        #         start += 1
        #         if start >= n:
        #             start = start % n
        #             a_round = True
        #         current_sum += gap[start]
        #     if start == end and current_sum >= 0:
        #         return (start + 1) % n
        #     start += 1
        # return -1
