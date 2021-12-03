
# 152. Maximum Product Subarray

# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
# https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity/160464


class Solution(object):
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]  # Store the result that is the max we found so far
        pos_temp, neg_temp = result, result

        for n in nums[1:]:
            candidates = (n, pos_temp * n, neg_temp * n)
            pos_temp = max(candidates)
            neg_temp = min(candidates)

            result = max(result, pos_temp)
        return result
