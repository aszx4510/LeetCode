
# 1010. Pairs of Songs With Total Durations Divisible by 60

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Concise version
        mods = defaultdict(int)  # defaultdict is faster than normal array
        ans = 0
        for t in time:
            m = t % 60
            if m == 0:
                ans += mods[m]
            else:
                ans += mods[60 - m]
            mods[m] += 1
        return ans


        # My method
        mods = [0] * 60
        for t in time:
            mods[t % 60] += 1

        ans = 0
        for i in range(1, 30):
            ans += mods[i] * mods[60 - i]
        ans += mods[0] * (mods[0] - 1) // 2
        ans += mods[30] * (mods[30] - 1) // 2

        return ans
