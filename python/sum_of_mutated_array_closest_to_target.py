
# 1300. Sum of Mutated Array Closest to Target

# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/Python-Sort-Solution
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463306/Python-Sort-Solution/418308


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # Sort and pop out interatively
        arr.sort(reverse=True)
        max_num = arr[0]

        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()

        if not arr:  # all values are smaller than target
            return max_num
        elif target / len(arr) - target // len(arr) <= 0.5:
            return target // len(arr)
        return target // len(arr) + 1
