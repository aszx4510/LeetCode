
# 169. Majority Element

# https://leetcode.com/problems/majority-element/description/
# Moore's voting algorithm 
# http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = None, 0
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            else:
                if num == majority:
                    count += 1
                else:
                    count -= 1
        return majority
