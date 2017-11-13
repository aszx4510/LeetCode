
# 628. Maximum Product of Three Numbers

# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
# https://discuss.leetcode.com/topic/94108/python-concise-solution-o-n-and-1-line


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        

        # concise version, Time Complexity: O(nlogn)
        nums.sort()  # increasing
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


        # my version, Time Complexity: O(n)
        from operator import mul
        from functools import reduce
        pos_max = [-1001, -1001, -1001]
        neg_max = [1001, 1001]
        for num in nums:
            if num > pos_max[0]:
                pos_max = [num, pos_max[0], pos_max[1]]
            elif num > pos_max[1]:
                pos_max = [pos_max[0], num, pos_max[1]]
            elif num > pos_max[2]:
                pos_max = [pos_max[0], pos_max[1], num]
            
            if num < neg_max[0]:
                neg_max = [num, neg_max[0]]
            elif num < neg_max[1]:
                neg_max = [neg_max[0], num]
        print(pos_max, neg_max)
        return max(reduce(mul, pos_max), reduce(mul, neg_max) * pos_max[0])
