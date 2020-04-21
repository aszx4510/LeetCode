
# # 30-Day LeetCoding Challenge: Week 2 Day 7
# Leftmost Column with at Least a One

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        result = m
        for i in range(n):
            left, right = 0, m - 1
            left_val, right_val = binaryMatrix.get(i, left), binaryMatrix.get(i, right)
            while left <= right:
                mid = (left + right) // 2
                mid_val = binaryMatrix.get(i, mid)
                if mid_val == 0:
                    print('if')
                    left = mid + 1
                else:
                    print('else')
                    right = mid - 1
            print(i, left)
            result = min(left, result)
        return result if result != m else -1
