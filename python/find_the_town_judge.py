
# 997. Find the Town Judge

# https://leetcode.com/problems/find-the-town-judge/
# https://leetcode.com/problems/find-the-town-judge/discuss/244859/Python-O(n)-with-Explanation


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # Concise version
        trusted = [0] * (N + 1)
        for x, y in trust:
            trusted[x] -= 1
            trusted[y] += 1

        for i in range(1, N + 1):
            if trusted[i] == N - 1:
                return i
        return -1


        # My method
        trust_count, trusted_count = defaultdict(int), defaultdict(int)
        for x, y in trust:
            trust_count[x] += 1
            trusted_count[y] += 1

        trust_flag = False
        for i in range(1, N + 1):
            if not trust_count[i] and trusted_count[i] == N - 1:
                return i
        return -1
