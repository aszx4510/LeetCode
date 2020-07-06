
# 368. Largest Divisible Subset

# https://leetcode.com/problems/largest-divisible-subset/
# https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1: set()}
        for x in sorted(nums):
            # At least x are divisible itself
            S[x] = max((S[d] for d in S.keys() if x % d == 0), key=len) | {x}
        return list(max((S[d] for d in S.keys()), key=len))
